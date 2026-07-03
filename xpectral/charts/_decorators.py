# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations
from datetime import date
from functools import wraps
from inspect import Parameter
from inspect import Signature
from inspect import signature

# Other imports
from bokeh.models import BasicTickFormatter
from bokeh.models import DatetimeTickFormatter
from bokeh.models.renderers import GlyphRenderer
from bokeh.plotting._docstring import generate_docstring
from bokeh.plotting._renderer import create_renderer
from .palette_manager import palette

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

# Glyph properties that carry a color; used to skip auto-color on glyphs that
# have none (e.g. the image glyphs), whose kwargs must stay free of `color`.
_COLOR_PROPS = frozenset({"line_color", "fill_color", "text_color", "hatch_color"})

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def glyph_method(glyphclass):
    def decorator(func):
        parameters = glyphclass.parameters()

        sigparams = (
            [Parameter("self", Parameter.POSITIONAL_OR_KEYWORD)]
            + [x[0] for x in parameters]
            + [Parameter("source", Parameter.KEYWORD_ONLY, default=None)]
            + [Parameter("legend", Parameter.KEYWORD_ONLY, default=True)]
            + [Parameter("kwargs", Parameter.VAR_KEYWORD)]
        )

        @wraps(func)
        def wrapped(self, *args, **kwargs):
            # Validate positional arguments against the glyph's declared positional field order.
            if len(args) > len(glyphclass._args):
                raise TypeError(
                    f"{func.__name__} takes {len(glyphclass._args)} positional argument but {len(args)} were given"
                )
            # Map positional inputs to their corresponding glyph kwargs by param name.
            for arg, param in zip(args, sigparams[1:]):
                kwargs[param.name] = arg
            # Pop `legend` before it reaches create_renderer — it is not a glyph property.
            legend = kwargs.pop("legend", True)
            # Default source comes from the accessor unless explicitly provided.
            kwargs.setdefault("source", self.source)
            # Preserve any coordinate context passed through a custom Figure subclass.
            if self.coordinates is not None:
                kwargs.setdefault("coordinates", self.coordinates)
            # Capture user-supplied x/y column names before any synthetic fallbacks are
            # injected, so synthetic field names ("x"/"y") are never used as legend labels.
            x_label = kwargs.get("x") if isinstance(kwargs.get("x"), str) else None
            y_label = kwargs.get("y") if isinstance(kwargs.get("y"), str) else None
            # Inspect/create synthetic fields on the source when required by the glyph.
            source = kwargs["source"]
            n = len(next(iter(source.data.values()), ()))
            # If x is required but missing, inject a 0..n-1 index column into source and reference it by name.
            if "x" in glyphclass._args and "x" not in kwargs and "x" not in source.data:
                source.data["x"] = list(range(n))
                kwargs["x"] = "x"
            # If y is required but missing, inject a 0..n-1 index column into source and reference it by name.
            if "y" in glyphclass._args and "y" not in kwargs and "y" not in source.data:
                source.data["y"] = list(range(n))
                kwargs["y"] = "y"
            # Auto-derive legend_label from the primary data column name, mirroring
            # pandas.DataFrame.plot(legend=True). Prefer y (the data axis for most
            # vertical glyphs), fall back to x. Skipped when the caller already supplied
            # legend_label, or when the value is not a string (e.g. a literal array or
            # a synthetic index column that was just injected above).
            if legend and "legend_label" not in kwargs:
                label = y_label or x_label
                if label is not None:
                    kwargs["legend_label"] = label
            # Auto-assign the next palette color when the caller left color unset,
            # mirroring pandas.DataFrame.plot()'s per-series color cycle. Keyed off
            # how many glyph renderers the plot already has, so successive calls —
            # and each stacker routed back through here — step through the palette.
            # Skipped for glyphs with no color property (e.g. images).
            if _is_colorable(glyphclass) and not _has_color(kwargs):
                kwargs["color"] = _cycle_color(self.plot)
            # Auto-format an axis as datetime when its coordinate column holds
            # date/datetime values, mirroring bokeh's x_axis_type="datetime". Only
            # replaces the default formatter, so an explicit datetime axis or a
            # user-set formatter is left untouched. Covers stacks too, since they
            # route their shared coordinate through here.
            if x_label is not None:
                _apply_datetime_axis(self.plot.xaxis, source, x_label)
            if y_label is not None:
                _apply_datetime_axis(self.plot.yaxis, source, y_label)
            # Delegate to Bokeh with normalized kwargs and possibly augmented source columns.
            return create_renderer(glyphclass, self.plot, **kwargs)

        wrapped.__signature__ = Signature(
            parameters=sigparams, return_annotation=signature(func).return_annotation
        )

        wrapped.__doc__ = generate_docstring(glyphclass, parameters, func.__doc__)

        return wrapped

    return decorator


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------


def _has_color(kwargs):
    # True when the caller already specified any color, so auto-color defers to
    # it. Covers the `color` shorthand and every prefixed color property
    # (line_color, fill_color, nonselection_fill_color, ...).
    return any(key == "color" or key.endswith("_color") for key in kwargs)


def _is_colorable(glyphclass):
    # True when the glyph has at least one color property. Excludes glyphs like
    # the image family, whose kwargs would otherwise carry an unusable `color`.
    return not _COLOR_PROPS.isdisjoint(glyphclass.properties())


def _cycle_color(plot):
    # Reimplements the working branch of bokeh's (private, otherwise-unused)
    # get_default_color against the public `plot.renderers`, delegating the
    # color list and wraparound to the settable global palette.
    n = sum(isinstance(renderer, GlyphRenderer) for renderer in plot.renderers)
    return palette.color(n)


def _is_datetime_column(source, name):
    # Whether the named source column holds date/datetime values. `date` also
    # matches datetime and pandas Timestamp (both subclass it), so this covers
    # Polars Date/Datetime and pandas datetime64 alike after the accessor's
    # date coercion. Judges by the first non-null value.
    for value in source.data.get(name, ()):
        if value is None:
            continue
        return isinstance(value, date)
    return False


def _apply_datetime_axis(axes, source, name):
    # Attach a datetime formatter to each axis whose coordinate is a datetime
    # column. Only the default BasicTickFormatter is replaced, so an explicit
    # datetime axis or a caller-set formatter is preserved.
    if not _is_datetime_column(source, name):
        return
    for axis in axes:
        if isinstance(axis.formatter, BasicTickFormatter):
            axis.formatter = DatetimeTickFormatter()
