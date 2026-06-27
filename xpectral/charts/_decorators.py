# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations
from functools import wraps
from inspect import Parameter
from inspect import Signature
from inspect import signature

# Other imports
from bokeh.plotting._docstring import generate_docstring
from bokeh.plotting._renderer import create_renderer

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def glyph_method(glyphclass):
    def decorator(func):
        parameters = glyphclass.parameters()

        # TODO: send issue so that this signature only takes glyphclass.args instead of [x[0] for x in parameters]
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
