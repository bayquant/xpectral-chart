# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from typing import Any, Callable, Sequence, Unpack

import pandas as pd
import polars as pl

# Other imports
from bokeh._specs import (
    AngleArg,
    DistanceArg,
    FloatArg,
    Image2dArg,
    Image3dArg,
    MarkerArg,
    NullDistanceArg,
    Number1dArg,
    Number3dArg,
    NumberArg,
    SizeArg,
    StringArg,
)
from bokeh.core.enums import DirectionType as Direction
from bokeh.io.notebook import CommsHandle, ProxyUrlFunc
from bokeh.models import ColumnDataSource, glyphs
from bokeh.models.renderers import GlyphRenderer
from bokeh.plotting import figure as _bokeh_figure
from bokeh.plotting.glyph_api import (
    AnnularWedgeArgs,
    AnnulusArgs,
    ArcArgs,
    BezierArgs,
    BlockArgs,
    EllipseArgs,
    HAreaArgs,
    HAreaStepArgs,
    HBarArgs,
    HexTileArgs,
    HSpanArgs,
    HStripArgs,
    ImageArgs,
    ImageRGBAArgs,
    ImageStackArgs,
    ImageURLArgs,
    LineArgs,
    MathMLArgs,
    MultiLineArgs,
    MultiPolygonsArgs,
    NgonArgs,
    PatchArgs,
    PatchesArgs,
    QuadArgs,
    QuadraticArgs,
    RayArgs,
    RectArgs,
    ScatterArgs,
    SegmentArgs,
    StepArgs,
    TeXArgs,
    TextArgs,
    VAreaArgs,
    VAreaStepArgs,
    VBarArgs,
    VSpanArgs,
    VStripArgs,
    WedgeArgs,
)
from bokeh.util.browser import BrowserTarget

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------

class BokehAccessor(_bokeh_figure):
    def __init__(self, df: pd.DataFrame | pl.DataFrame) -> None: ...
    @classmethod
    def register(cls, func: Callable[..., Any]) -> Callable[..., Any]: ...
    @property
    def source(self) -> ColumnDataSource: ...
    def show(
        self,
        browser: str | None = ...,
        new: BrowserTarget = ...,
        notebook_handle: bool = ...,
        notebook_url: str | ProxyUrlFunc = ...,
        **kwargs: Any,
    ) -> CommsHandle | None: ...

    # Untyped on purpose: this is an internal construction step, never the
    # user-facing entry point. `figure()` in `xpectral_chart/__init__.py` is
    # the typed, documented way to pass figure kwargs (title, width, tools,
    # ...); it forwards them here as **kwargs after resolving its own,
    # fully-typed, named parameters.
    def __call__(self, **kwargs: Any) -> BokehAccessor: ...

    # Glyph methods with both x and y parameters

    def annular_wedge(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        inner_radius: DistanceArg = ...,
        outer_radius: DistanceArg = ...,
        start_angle: AngleArg = ...,
        end_angle: AngleArg = ...,
        direction: Direction = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[AnnularWedgeArgs],
    ) -> GlyphRenderer[glyphs.AnnularWedge]: ...
    def annulus(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        inner_radius: DistanceArg = ...,
        outer_radius: DistanceArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[AnnulusArgs],
    ) -> GlyphRenderer[glyphs.Annulus]: ...
    def arc(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        radius: DistanceArg = ...,
        start_angle: AngleArg = ...,
        end_angle: AngleArg = ...,
        direction: Direction = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ArcArgs],
    ) -> GlyphRenderer[glyphs.Arc]: ...
    def block(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        width: DistanceArg = ...,
        height: DistanceArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[BlockArgs],
    ) -> GlyphRenderer[glyphs.Block]: ...
    def ellipse(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        width: DistanceArg = ...,
        height: DistanceArg = ...,
        angle: AngleArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[EllipseArgs],
    ) -> GlyphRenderer[glyphs.Ellipse]: ...
    def image(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        image: Image2dArg = ...,
        x: NumberArg = ...,
        y: NumberArg = ...,
        dw: DistanceArg = ...,
        dh: DistanceArg = ...,
        dilate: bool = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ImageArgs],
    ) -> GlyphRenderer[glyphs.Image]: ...
    def image_rgba(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        image: Image2dArg = ...,
        x: NumberArg = ...,
        y: NumberArg = ...,
        dw: DistanceArg = ...,
        dh: DistanceArg = ...,
        dilate: bool = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ImageRGBAArgs],
    ) -> GlyphRenderer[glyphs.ImageRGBA]: ...
    def image_stack(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        image: Image3dArg = ...,
        x: NumberArg = ...,
        y: NumberArg = ...,
        dw: DistanceArg = ...,
        dh: DistanceArg = ...,
        dilate: bool = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ImageStackArgs],
    ) -> GlyphRenderer[glyphs.ImageStack]: ...
    def image_url(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        url: StringArg = ...,
        x: NumberArg = ...,
        y: NumberArg = ...,
        w: NullDistanceArg = ...,
        h: NullDistanceArg = ...,
        angle: AngleArg = ...,
        dilate: bool = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ImageURLArgs],
    ) -> GlyphRenderer[glyphs.ImageURL]: ...
    def line(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[LineArgs],
    ) -> GlyphRenderer[glyphs.Line]: ...
    def mathml_glyph(
        self,
        x: NumberArg = ...,
        y: NumberArg = ...,
        text: StringArg = ...,
        angle: AngleArg = ...,
        x_offset: FloatArg = ...,
        y_offset: FloatArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[MathMLArgs],
    ) -> GlyphRenderer[glyphs.MathMLGlyph]: ...
    def ngon(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        radius: DistanceArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[NgonArgs],
    ) -> GlyphRenderer[glyphs.Ngon]: ...
    def patch(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[PatchArgs],
    ) -> GlyphRenderer[glyphs.Patch]: ...
    def ray(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        length: DistanceArg = ...,
        angle: AngleArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[RayArgs],
    ) -> GlyphRenderer[glyphs.Ray]: ...
    def rect(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        width: DistanceArg = ...,
        height: DistanceArg = ...,
        angle: AngleArg = ...,
        dilate: bool = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[RectArgs],
    ) -> GlyphRenderer[glyphs.Rect]: ...
    def scatter(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        size: SizeArg = ...,
        angle: AngleArg = ...,
        marker: MarkerArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[ScatterArgs],
    ) -> GlyphRenderer[glyphs.Scatter]: ...
    def step(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[StepArgs],
    ) -> GlyphRenderer[glyphs.Step]: ...
    def tex_glyph(
        self,
        x: NumberArg = ...,
        y: NumberArg = ...,
        text: StringArg = ...,
        angle: AngleArg = ...,
        x_offset: FloatArg = ...,
        y_offset: FloatArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[TeXArgs],
    ) -> GlyphRenderer[glyphs.TeXGlyph]: ...
    def text(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        text: StringArg = ...,
        angle: AngleArg = ...,
        x_offset: FloatArg = ...,
        y_offset: FloatArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[TextArgs],
    ) -> GlyphRenderer[glyphs.Text]: ...
    def wedge(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y: NumberArg = ...,
        radius: DistanceArg = ...,
        start_angle: AngleArg = ...,
        end_angle: AngleArg = ...,
        direction: Direction = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[WedgeArgs],
    ) -> GlyphRenderer[glyphs.Wedge]: ...

    # Vertical glyph methods (have parameter x but not y)

    def varea(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y1: NumberArg = ...,
        y2: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[VAreaArgs],
    ) -> GlyphRenderer[glyphs.VArea]: ...
    def varea_step(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        y1: NumberArg = ...,
        y2: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[VAreaStepArgs],
    ) -> GlyphRenderer[glyphs.VAreaStep]: ...
    def vbar(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        width: DistanceArg = ...,
        top: NumberArg = ...,
        bottom: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[VBarArgs],
    ) -> GlyphRenderer[glyphs.VBar]: ...
    def vspan(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[VSpanArgs],
    ) -> GlyphRenderer[glyphs.VSpan]: ...

    # Horizontal glyph methods (have parameter y but not x)

    def harea(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x1: NumberArg = ...,
        x2: NumberArg = ...,
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HAreaArgs],
    ) -> GlyphRenderer[glyphs.HArea]: ...
    def harea_step(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x1: NumberArg = ...,
        x2: NumberArg = ...,
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HAreaStepArgs],
    ) -> GlyphRenderer[glyphs.HAreaStep]: ...
    def hbar(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        y: NumberArg = ...,
        height: DistanceArg = ...,
        right: NumberArg = ...,
        left: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HBarArgs],
    ) -> GlyphRenderer[glyphs.HBar]: ...
    def hspan(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        y: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HSpanArgs],
    ) -> GlyphRenderer[glyphs.HSpan]: ...

    # Glyph methods without x nor y parameters

    def bezier(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x0: NumberArg = ...,
        y0: NumberArg = ...,
        x1: NumberArg = ...,
        y1: NumberArg = ...,
        cx0: NumberArg = ...,
        cy0: NumberArg = ...,
        cx1: NumberArg = ...,
        cy1: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[BezierArgs],
    ) -> GlyphRenderer[glyphs.Bezier]: ...
    def hstrip(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        y0: NumberArg = ...,
        y1: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HStripArgs],
    ) -> GlyphRenderer[glyphs.HStrip]: ...
    def hextile(
        self,
        q: NumberArg = ...,
        r: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[HexTileArgs],
    ) -> GlyphRenderer[glyphs.HexTile]: ...
    def multi_line(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        xs: Number1dArg = ...,
        ys: Number1dArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[MultiLineArgs],
    ) -> GlyphRenderer[glyphs.MultiLine]: ...
    def multipolygons(
        self,
        xs: Number3dArg = ...,
        ys: Number3dArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[MultiPolygonsArgs],
    ) -> GlyphRenderer[glyphs.MultiPolygons]: ...
    def patches(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        xs: Number1dArg = ...,
        ys: Number1dArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[PatchesArgs],
    ) -> GlyphRenderer[glyphs.Patches]: ...
    def quad(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        left: NumberArg = ...,
        right: NumberArg = ...,
        top: NumberArg = ...,
        bottom: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[QuadArgs],
    ) -> GlyphRenderer[glyphs.Quad]: ...
    def quadratic(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x0: NumberArg = ...,
        y0: NumberArg = ...,
        x1: NumberArg = ...,
        y1: NumberArg = ...,
        cx: NumberArg = ...,
        cy: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[QuadraticArgs],
    ) -> GlyphRenderer[glyphs.Quadratic]: ...
    def segment(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x0: NumberArg = ...,
        y0: NumberArg = ...,
        x1: NumberArg = ...,
        y1: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[SegmentArgs],
    ) -> GlyphRenderer[glyphs.Segment]: ...
    def vstrip(
        self,  # pyright: ignore[reportIncompatibleMethodOverride]
        x0: NumberArg = ...,
        x1: NumberArg = ...,
        *,
        auto_legend: bool = ...,
        **kwargs: Unpack[VStripArgs],
    ) -> GlyphRenderer[glyphs.VStrip]: ...

    # Stack methods

    def harea_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.HArea]]: ...
    def hbar_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.HBar]]: ...
    def hline_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.Line]]: ...
    def varea_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.VArea]]: ...
    def vbar_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.VBar]]: ...
    def vline_stack(
        self, stackers: Sequence[str] | None = ..., *, auto_legend: bool = ..., **kwargs
    ) -> list[GlyphRenderer[glyphs.Line]]: ...
