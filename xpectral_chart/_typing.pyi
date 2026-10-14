# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from typing import Literal, Sequence, TypeAlias

# Third-party imports
from bokeh.core.enums import AutoType as Auto
from bokeh.core.properties import Datetime, TimeDelta
from bokeh.models.ranges import Range

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
