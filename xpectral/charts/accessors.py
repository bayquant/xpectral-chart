# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations
import warnings
from datetime import date
from datetime import datetime
from datetime import time
from typing import Any
from typing import Callable
from typing import Self
from typing import Sequence

# Other imports
from bokeh.models import ColumnDataSource
from bokeh.models import glyphs
from bokeh.models.renderers import GlyphRenderer
from bokeh.plotting._stack import double_stack
from bokeh.plotting._stack import single_stack
from bokeh.util.warnings import BokehUserWarning
import pandas as pd
import polars as pl
from ._decorators import glyph_method
from ._figure import Figure

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

warnings.simplefilter("ignore", BokehUserWarning)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


class BokehAccessor(Figure):

    def __init__(self, df) -> None:
        self._df = df

    def __call__(self, *args, **kwargs) -> Self:
        super().__init__(*args, **kwargs)
        return self.plot

    @classmethod
    def register(cls, func: Callable[..., Any]) -> Callable[..., Any]:
        """Register a function as a method on the accessor.

        Use as a decorator to add custom chart methods to all
        ``BokehAccessor`` subclasses (both Pandas and Polars variants).
        The decorated function's first parameter must be ``self`` — the
        accessor instance — which exposes ``self._df``, ``self.source``,
        ``self.plot``, and every built-in glyph method.

        Args:
            func: Function to register.  Its first argument must be
                ``self`` (the accessor instance).

        Returns:
            The original function, unchanged.

        Example::

            @BokehAccessor.register
            def candlestick(self, open, high, low, close, **kwargs):
                mid = (open + close) / 2
                self.segment(x0=self._df["date"], y0=high,
                             x1=self._df["date"], y1=low, **kwargs)
                return self.rect(x="date", y=mid, width=0.5,
                                 height=abs(close - open), **kwargs)
        """
        setattr(cls, func.__name__, func)
        return func

    # -------------------------------------------
    # Glyph methods with both x and y parameters
    @glyph_method(glyphs.AnnularWedge)
    def annular_wedge(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/annular_wedge.html
        """

    @glyph_method(glyphs.Annulus)
    def annulus(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/annulus.html
        """

    @glyph_method(glyphs.Arc)
    def arc(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/arc.html
        """

    @glyph_method(glyphs.Block)
    def block(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/block.html
        """

    @glyph_method(glyphs.Ellipse)
    def ellipse(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ellipse.html
        """

    @glyph_method(glyphs.Image)
    def image(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image.html
        """

    @glyph_method(glyphs.ImageRGBA)
    def image_rgba(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_rgba.html
        """

    @glyph_method(glyphs.ImageStack)
    def image_stack(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_stack.html
        """

    @glyph_method(glyphs.ImageURL)
    def image_url(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_url.html
        """

    @glyph_method(glyphs.Line)
    def line(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html
        """

    @glyph_method(glyphs.MathMLGlyph)
    def mathml_glyph(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/math_ml.html
        """

    @glyph_method(glyphs.Ngon)
    def ngon(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ngon.html
        """

    @glyph_method(glyphs.Patch)
    def patch(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/patch.html
        """

    @glyph_method(glyphs.Ray)
    def ray(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/ray.html
        """

    @glyph_method(glyphs.Rect)
    def rect(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/rect.html
        """

    @glyph_method(glyphs.Scatter)
    def scatter(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/scatter.html
        """

    @glyph_method(glyphs.Step)
    def step(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/step.html
        """

    @glyph_method(glyphs.TeXGlyph)
    def tex_glyph(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/tex.html
        """

    @glyph_method(glyphs.Text)
    def text(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/text.html
        """

    @glyph_method(glyphs.Wedge)
    def wedge(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/wedge.html
        """

    # ----------------------------------------------------
    # Vertical glyph methods (have parameter x but not y)
    @glyph_method(glyphs.VArea)
    def varea(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/varea.html
        """

    @glyph_method(glyphs.VAreaStep)
    def varea_step(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/varea_step.html
        """

    @glyph_method(glyphs.VBar)
    def vbar(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vbar.html
        """

    @glyph_method(glyphs.VSpan)
    def vspan(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vspan.html
        """

    # ------------------------------------------------------
    # Horizontal glyph methods (have parameter y but not x)
    @glyph_method(glyphs.HArea)
    def harea(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/harea.html
        """

    @glyph_method(glyphs.HAreaStep)
    def harea_step(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/harea_step.html
        """

    @glyph_method(glyphs.HBar)
    def hbar(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hbar.html
        """

    @glyph_method(glyphs.HSpan)
    def hspan(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hspan.html
        """

    # -----------------------------------------
    # Glyph methods without x nor y parameters
    @glyph_method(glyphs.Bezier)
    def bezier(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/bezier.html
        """

    @glyph_method(glyphs.HStrip)
    def hstrip(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hstrip.html
        """

    @glyph_method(glyphs.HexTile)
    def hextile(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hex_tile.html
        """

    @glyph_method(glyphs.MultiLine)
    def multi_line(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/multi_line.html
        """

    @glyph_method(glyphs.MultiPolygons)
    def multipolygons(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/multi_polygons.html
        """

    @glyph_method(glyphs.Patches)
    def patches(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/patches.html
        """

    @glyph_method(glyphs.Quad)
    def quad(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/quad.html
        """

    @glyph_method(glyphs.Quadratic)
    def quadratic(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/quadratic.html
        """

    @glyph_method(glyphs.Segment)
    def segment(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/segment.html
        """

    @glyph_method(glyphs.VStrip)
    def vstrip(self, *args: Any, **kwargs: Any) -> GlyphRenderer:
        """See Also:
        https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vstrip.html
        """

    # -----------------------------------------
    # Glyph stack methods
    def harea_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack horizontal filled areas between consecutive stacker columns.

        Each stacker column is cumulated left-to-right: the running total
        before the current stacker becomes ``x1`` and after becomes ``x2``,
        producing one filled band per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``y``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`harea`
                (e.g. ``y``, ``fill_color``, ``fill_alpha``). If ``y`` is
                not given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/harea.html
        """
        if "y" not in kwargs:
            kwargs["y"] = _ensure_default_coord(self.source, "y")
        stackers = _resolve_stackers(self._df, stackers, kwargs["y"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in double_stack(stackers=stackers, spec0="x1", spec1="x2", **kwargs):
            result.append(self.harea(**kwarg))
        return result

    def hbar_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack horizontal bars between consecutive stacker columns.

        Each stacker column is cumulated left-to-right: the running total
        before the current stacker becomes ``left`` and after becomes ``right``,
        producing one bar segment per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``y``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`hbar`
                (e.g. ``y``, ``height``, ``fill_color``). If ``y`` is not
                given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/hbar.html
        """
        if "y" not in kwargs:
            kwargs["y"] = _ensure_default_coord(self.source, "y")
        stackers = _resolve_stackers(self._df, stackers, kwargs["y"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in double_stack(
            stackers=stackers, spec0="left", spec1="right", **kwargs
        ):
            result.append(self.hbar(**kwarg))
        return result

    def hline_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack horizontal lines at the cumulative sum of each stacker column.

        Each stacker column is cumulated left-to-right and the running total
        is used as the ``x`` coordinate, producing one line per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``y``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`line`
                (e.g. ``y``, ``line_color``, ``line_width``). If ``y`` is
                not given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html
        """
        if "y" not in kwargs:
            kwargs["y"] = _ensure_default_coord(self.source, "y")
        stackers = _resolve_stackers(self._df, stackers, kwargs["y"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in single_stack(stackers=stackers, spec="x", **kwargs):
            result.append(self.line(**kwarg))
        return result

    def varea_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack vertical filled areas between consecutive stacker columns.

        Each stacker column is cumulated bottom-to-top: the running total
        before the current stacker becomes ``y1`` and after becomes ``y2``,
        producing one filled band per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``x``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`varea`
                (e.g. ``x``, ``fill_color``, ``fill_alpha``). If ``x`` is
                not given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/varea.html
        """
        if "x" not in kwargs:
            kwargs["x"] = _ensure_default_coord(self.source, "x")
        stackers = _resolve_stackers(self._df, stackers, kwargs["x"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in double_stack(stackers=stackers, spec0="y1", spec1="y2", **kwargs):
            result.append(self.varea(**kwarg))
        return result

    def vbar_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack vertical bars between consecutive stacker columns.

        Each stacker column is cumulated bottom-to-top: the running total
        before the current stacker becomes ``bottom`` and after becomes ``top``,
        producing one bar segment per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``x``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`vbar`
                (e.g. ``x``, ``width``, ``fill_color``). If ``x`` is not
                given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/vbar.html
        """
        if "x" not in kwargs:
            kwargs["x"] = _ensure_default_coord(self.source, "x")
        stackers = _resolve_stackers(self._df, stackers, kwargs["x"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in double_stack(
            stackers=stackers, spec0="bottom", spec1="top", **kwargs
        ):
            result.append(self.vbar(**kwarg))
        return result

    def vline_stack(
        self,
        stackers: Sequence[str] | None = None,
        *,
        legend: bool = True,
        **kwargs: Any,
    ) -> list[GlyphRenderer]:
        """Stack vertical lines at the cumulative sum of each stacker column.

        Each stacker column is cumulated bottom-to-top and the running total
        is used as the ``y`` coordinate, producing one line per stacker.

        Args:
            stackers: Column names to stack in order. If not given, stacks
                every numeric column of the underlying DataFrame except
                whichever column is passed as ``x``.
            legend: Whether to label each stacker with its column name when
                ``legend_label`` isn't given explicitly, mirroring
                ``pandas.DataFrame.plot()``'s ``legend`` parameter.
            **kwargs: Visual properties forwarded to :meth:`line`
                (e.g. ``x``, ``line_color``, ``line_width``). If ``x`` is
                not given, defaults to a 0-based range index.

        Returns:
            One :class:`~bokeh.models.renderers.GlyphRenderer` per stacker.

        See Also:
            https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html
        """
        if "x" not in kwargs:
            kwargs["x"] = _ensure_default_coord(self.source, "x")
        stackers = _resolve_stackers(self._df, stackers, kwargs["x"])
        _apply_auto_legend(kwargs, stackers, legend)
        result = []
        for kwarg in single_stack(stackers=stackers, spec="y", **kwargs):
            result.append(self.line(**kwarg))
        return result


@pl.api.register_dataframe_namespace("bokeh")
class PolarsBokehAccessor(BokehAccessor):

    __view_model__ = "Figure"
    __view_module__ = "bokeh.plotting.figure"

    @property
    def source(self) -> ColumnDataSource:
        if not hasattr(self, "_source"):
            data = _coerce_unsafe_dates(self._df.to_dict(as_series=False))
            self._source = ColumnDataSource(data)
        return self._source


@pd.api.extensions.register_dataframe_accessor("bokeh")
class PandasBokehAccessor(BokehAccessor):

    __view_model__ = "Figure"
    __view_module__ = "bokeh.plotting.figure"

    @property
    def source(self) -> ColumnDataSource:
        if not hasattr(self, "_source"):
            data = _coerce_unsafe_dates(self._df.to_dict(orient="list"))
            self._source = ColumnDataSource(data)
        return self._source


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------


def _coerce_unsafe_dates(data: dict[str, list[Any]]) -> dict[str, list[Any]]:
    # Bokeh's serializer encodes bare `datetime.date` values as ISO date
    # strings rather than millisecond timestamps (unlike `datetime.datetime`,
    # which it converts to numbers), which silently breaks glyph positioning
    # on any numeric axis (see bokeh.core.serialization.Serializer._encode_other).
    # Promote bare dates to midnight datetimes so columns are numeric-safe
    # regardless of source: Polars `Date` columns, or pandas `object`-dtype
    # columns of raw `date`s (e.g. from `.dt.date`).
    for column, values in data.items():
        if any(isinstance(v, date) and not isinstance(v, datetime) for v in values):
            data[column] = [
                (
                    datetime.combine(v, time.min)
                    if isinstance(v, date) and not isinstance(v, datetime)
                    else v
                )
                for v in values
            ]
    return data


def _numeric_columns(df: pd.DataFrame | pl.DataFrame) -> list[str]:
    # Mirrors pandas.DataFrame.plot()'s default column selection for
    # plotting: numeric dtypes only (bool, string, date/datetime, etc.
    # are excluded).
    if isinstance(df, pl.DataFrame):
        return [name for name, dtype in df.schema.items() if dtype.is_numeric()]
    return list(df.select_dtypes(include="number").columns)


def _resolve_stackers(
    df: pd.DataFrame | pl.DataFrame, stackers: Sequence[str] | None, coordinate: Any
) -> Sequence[str]:
    # When `stackers` isn't given, stack every numeric column except the
    # one explicitly used as the shared coordinate (x for vertical stacks,
    # y for horizontal stacks), mirroring pandas.DataFrame.plot()'s default
    # of plotting every numeric column.
    if stackers is not None:
        return stackers
    numeric = _numeric_columns(df)
    if isinstance(coordinate, str):
        numeric = [c for c in numeric if c != coordinate]
    return numeric


def _ensure_default_coord(source: ColumnDataSource, key: str) -> str:
    # Ensures a 0-based range column exists under `key` in the source,
    # mirroring the same convention used in _decorators.py's glyph_method
    # wrapper. Both paths now use identical semantics (0-based, named "x"/"y")
    # so there is no divergence between individual glyph calls and stack calls.
    if key not in source.data:
        n = len(next(iter(source.data.values()), ()))
        source.data[key] = list(range(n))
    return key


def _apply_auto_legend(
    kwargs: dict[str, Any], stackers: Sequence[str], legend: bool
) -> None:
    # Mirrors pandas.DataFrame.plot(legend=True): label each stacked series
    # with its column name when no explicit legend_label is given.
    # Has no effect when the caller already supplied legend_label.
    if legend and "legend_label" not in kwargs:
        kwargs["legend_label"] = list(stackers)
    elif not legend:
        # Forward legend=False into the per-stacker glyph kwargs so the
        # glyph_method decorator doesn't re-enable auto-legend with its
        # own default of legend=True.
        kwargs["legend"] = False


# Polars' NameSpace descriptor caches the accessor on the DataFrame instance
# via setattr, causing the same BokehAccessor to be returned on repeated
# accesses of df.bokeh. Replacing the descriptor with a non-caching property
# ensures each access produces a fresh instance.
pl.DataFrame.bokeh = property(lambda self: PolarsBokehAccessor(self))  # type: ignore[assignment]
