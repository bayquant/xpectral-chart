# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from typing import Any, Sequence

# Third-party imports
import pandas as pd
import polars as pl
from bokeh.core.enums import AutoType as Auto
from bokeh.core.enums import HorizontalLocationType as HorizontalLocation
from bokeh.core.enums import LocationType as Location
from bokeh.core.enums import SizingModeType as SizingMode
from bokeh.core.enums import VerticalLocationType as VerticalLocation
from bokeh.core.properties import Color, TextLike
from bokeh.models.dom import Template
from bokeh.models.tools import Drag, GestureTool, InspectTool, Scroll, Tap, Tool

from .._typing import AxisType, PandasDataFrame, PolarsDataFrame, RangeLike

# Local imports
from .accessors import BokehAccessor, PandasBokehAccessor, PolarsBokehAccessor

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

__all__ = [
    "BokehAccessor",
    "PandasBokehAccessor",
    "PandasDataFrame",
    "PolarsBokehAccessor",
    "PolarsDataFrame",
    "figure",
]


class _Unset:
    __slots__ = ()

    def __repr__(self) -> str:
        return "..."


_UNSET: Any = _Unset()

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def figure(
    df: pl.DataFrame | pd.DataFrame,
    *,
    x_range: RangeLike = _UNSET,
    y_range: RangeLike = _UNSET,
    x_axis_type: AxisType = _UNSET,
    y_axis_type: AxisType = _UNSET,
    tools: str | Sequence[str | Tool] = _UNSET,
    x_minor_ticks: Auto | int = _UNSET,
    y_minor_ticks: Auto | int = _UNSET,
    x_axis_location: VerticalLocation | None = _UNSET,
    y_axis_location: HorizontalLocation | None = _UNSET,
    x_axis_label: TextLike | None = _UNSET,
    y_axis_label: TextLike | None = _UNSET,
    active_drag: Auto | str | Drag | None = _UNSET,
    active_inspect: Auto | str | InspectTool | Sequence[InspectTool] | None = _UNSET,
    active_scroll: Auto | str | Scroll | None = _UNSET,
    active_tap: Auto | str | Tap | None = _UNSET,
    active_multi: Auto | str | GestureTool | None = _UNSET,
    tooltips: Template | str | list[tuple[str, str]] | None = _UNSET,
    width: int = _UNSET,
    height: int = _UNSET,
    frame_width: int = _UNSET,
    frame_height: int = _UNSET,
    min_width: int = _UNSET,
    max_width: int = _UNSET,
    min_height: int = _UNSET,
    max_height: int = _UNSET,
    sizing_mode: SizingMode = _UNSET,
    aspect_ratio: float | Auto = _UNSET,
    match_aspect: bool = _UNSET,
    title: str | None = _UNSET,
    title_location: Location = _UNSET,
    toolbar_location: Location | None = _UNSET,
    toolbar_inner: bool = _UNSET,
    toolbar_sticky: bool = _UNSET,
    background_fill_color: Color = _UNSET,
    background_fill_alpha: float = _UNSET,
    border_fill_color: Color = _UNSET,
    border_fill_alpha: float = _UNSET,
    outline_line_color: Color | None = _UNSET,
    outline_line_alpha: float = _UNSET,
    outline_line_width: float = _UNSET,
    min_border: int = _UNSET,
    min_border_top: int = _UNSET,
    min_border_bottom: int = _UNSET,
    min_border_left: int = _UNSET,
    min_border_right: int = _UNSET,
) -> BokehAccessor:
    """Create a Bokeh figure from a Polars or Pandas DataFrame.

    Equivalent to ``df.bokeh(**kwargs)`` but works with any DataFrame expression
    without requiring a typed intermediate variable.

    Args:
        df: A Polars or Pandas DataFrame.

    Returns:
        A :class:`~xpectral.charts.BokehAccessor` bound to ``df``, ready for
        glyph calls (e.g. :meth:`~BokehAccessor.vline_stack`, :meth:`~BokehAccessor.line`).

    Example::

        fig = figure(df.drop("step"), title="My chart", width=700)
        fig.vline_stack(color=Sunset10)
        fig.show()
    """
    kwargs = {
        k: v for k, v in locals().items() if not isinstance(v, _Unset) and k != "df"
    }
    if isinstance(df, pl.DataFrame):
        return PolarsBokehAccessor(df)(**kwargs)
    return PandasBokehAccessor(df)(**kwargs)


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------
