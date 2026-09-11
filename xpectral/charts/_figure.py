# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Future imports
from __future__ import annotations

# Standard library imports
import warnings
from typing import Self

# Third-party imports
from bokeh.models import Plot
from bokeh.plotting._figure import FigureOptions
from bokeh.plotting._plot import get_range, get_scale, process_axis_and_grid
from bokeh.plotting._tools import process_active_tools, process_tools_arg
from bokeh.util.warnings import BokehUserWarning

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

# Masquerading as "bokeh.plotting.figure.Figure" below (needed so Bokeh
# resolves our subclasses to its own JS view rather than crashing trying to
# build a nonexistent extension bundle for us) makes Bokeh emit a duplicate
# qualified-model warning at class-definition time; it's expected and harmless.
warnings.simplefilter("ignore", BokehUserWarning)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


class Figure(Plot):
    # Bokeh's HasProps.__init_subclass__ only checks the defining class's own
    # __dict__ for these, so every subclass needs its own explicit copy;
    # inheriting them from a base class doesn't count. Without this, Bokeh
    # derives __view_module__ from cls.__module__ (e.g. "xpectral.charts._figure"),
    # and since `xpectral` is a namespace package with no __file__, anything
    # that walks the model registry (e.g. output_notebook()) crashes trying
    # to resolve a JS extension bundle for it.
    __view_model__ = "Figure"
    __view_module__ = "bokeh.plotting.figure"

    def __init__(self, *arg, **kwargs) -> None:
        opts = FigureOptions(kwargs)

        names = self.properties()
        for name in kwargs.keys():
            if name not in names:
                self._raise_attribute_error_with_matches(
                    name, names | opts.properties()
                )

        super().__init__(*arg, **kwargs)

        self.x_range = get_range(opts.x_range)
        self.y_range = get_range(opts.y_range)

        self.x_scale = get_scale(self.x_range, opts.x_axis_type)
        self.y_scale = get_scale(self.y_range, opts.y_axis_type)

        process_axis_and_grid(
            self,
            opts.x_axis_type,
            opts.x_axis_location,
            opts.x_minor_ticks,
            opts.x_axis_label,
            self.x_range,
            0,
        )
        process_axis_and_grid(
            self,
            opts.y_axis_type,
            opts.y_axis_location,
            opts.y_minor_ticks,
            opts.y_axis_label,
            self.y_range,
            1,
        )

        tool_objs, tool_map = process_tools_arg(self, opts.tools, opts.tooltips)
        self.add_tools(*tool_objs)
        process_active_tools(
            self.toolbar,
            tool_map,
            opts.active_drag,
            opts.active_inspect,
            opts.active_scroll,
            opts.active_tap,
            opts.active_multi,
        )

    @property
    def plot(self) -> Self:
        return self

    @property
    def coordinates(self):
        return None


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------
