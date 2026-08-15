# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Future imports
from __future__ import annotations

# Standard library imports
from typing import Any, Literal, Protocol, Sequence, TypeAlias, TypeVar

# Third-party imports
from bokeh.core.enums import AutoType as Auto
from bokeh.core.enums import HorizontalLocationType as HorizontalLocation
from bokeh.core.enums import LocationType as Location
from bokeh.core.enums import SizingModeType as SizingMode
from bokeh.core.enums import VerticalLocationType as VerticalLocation
from bokeh.core.properties import Color, Datetime, TextLike, TimeDelta
from bokeh.models.dom import Template
from bokeh.models.ranges import Range
from bokeh.models.tools import Drag, GestureTool, InspectTool, Scroll, Tap, Tool

# Local imports
from .charts.accessors import PandasBokehAccessor, PolarsBokehAccessor

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

RangeLike: TypeAlias = (
    Range
    | tuple[float, float]
    | tuple[Datetime, Datetime]
    | tuple[TimeDelta, TimeDelta]
    | Sequence[str]
)

AxisType: TypeAlias = (
    Auto | Literal["linear", "log", "datetime", "timedelta", "mercator"] | None
)

T_BokehAccessor = TypeVar("T_BokehAccessor", PandasBokehAccessor, PolarsBokehAccessor)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


class BokehDataFrame(Protocol[T_BokehAccessor]):
    def bokeh(
        self,
        *,
        x_range: RangeLike = ...,
        y_range: RangeLike = ...,
        x_axis_type: AxisType = ...,
        y_axis_type: AxisType = ...,
        tools: str | Sequence[str | Tool] = ...,
        x_minor_ticks: Auto | int = ...,
        y_minor_ticks: Auto | int = ...,
        x_axis_location: VerticalLocation | None = ...,
        y_axis_location: HorizontalLocation | None = ...,
        x_axis_label: TextLike | None = ...,
        y_axis_label: TextLike | None = ...,
        active_drag: Auto | str | Drag | None = ...,
        active_inspect: Auto | str | InspectTool | Sequence[InspectTool] | None = ...,
        active_scroll: Auto | str | Scroll | None = ...,
        active_tap: Auto | str | Tap | None = ...,
        active_multi: Auto | str | GestureTool | None = ...,
        tooltips: Template | str | list[tuple[str, str]] | None = ...,
        width: int = ...,
        height: int = ...,
        frame_width: int = ...,
        frame_height: int = ...,
        min_width: int = ...,
        max_width: int = ...,
        min_height: int = ...,
        max_height: int = ...,
        sizing_mode: SizingMode = ...,
        aspect_ratio: float | Auto = ...,
        match_aspect: bool = ...,
        title: str | None = ...,
        title_location: Location = ...,
        toolbar_location: Location | None = ...,
        toolbar_inner: bool = ...,
        toolbar_sticky: bool = ...,
        background_fill_color: Color = ...,
        background_fill_alpha: float = ...,
        border_fill_color: Color = ...,
        border_fill_alpha: float = ...,
        outline_line_color: Color | None = ...,
        outline_line_alpha: float = ...,
        outline_line_width: float = ...,
        min_border: int = ...,
        min_border_top: int = ...,
        min_border_bottom: int = ...,
        min_border_left: int = ...,
        min_border_right: int = ...,
        **kwargs: Any,
    ) -> T_BokehAccessor:
        """Bokeh accessor for DataFrames.

        Call the accessor to create a figure, then chain glyph methods to build the plot.

        >>> fig = df.bokeh(...).line(...)
        """
        ...


class PolarsDataFrame(BokehDataFrame[PolarsBokehAccessor], Protocol): ...


class PandasDataFrame(BokehDataFrame[PandasBokehAccessor], Protocol): ...
