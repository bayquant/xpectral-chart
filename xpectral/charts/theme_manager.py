"""Central theme management for Bokeh apps."""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations

# Other imports
from bokeh.io import curdoc
from bokeh.themes import built_in_themes
from bokeh.themes import Theme

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

DEFAULT_THEME = "light_minimal"

THEMES = {
    "caliber": built_in_themes["caliber"],
    "carbon": built_in_themes["carbon"],
    "light_minimal": built_in_themes["light_minimal"],
    "dark_minimal": built_in_themes["dark_minimal"],
    "night_sky": built_in_themes["night_sky"],
    "contrast": built_in_themes["contrast"],
    "ocean": Theme(
        json={
            "attrs": {
                "Toolbar": {"logo": None},
                "Plot": {
                    "background_fill_color": "#e8e8ea",
                    "border_fill_color": "#e8e8ea",
                    "outline_line_color": "#253d8f",
                    "outline_line_alpha": 0.3,
                    "min_border_left": 36,
                    "min_border_right": 24,
                    "min_border_top": 26,
                    "min_border_bottom": 36,
                },
                "Grid": {
                    "grid_line_color": "#497bbc",
                    "grid_line_alpha": 0.2,
                },
                "Axis": {
                    "major_tick_line_alpha": 0.35,
                    "major_tick_line_color": "#6b7ab0",
                    "minor_tick_line_alpha": 0.25,
                    "minor_tick_line_color": "#6b7ab0",
                    "axis_line_alpha": 0.5,
                    "axis_line_color": "#6b7ab0",
                    "major_label_text_color": "#4d4d4d",
                    "major_label_text_font": "Helvetica",
                    "major_label_text_font_size": "1.025em",
                    "axis_label_standoff": 5,
                    "axis_label_text_color": "#6b7ab0",
                    "axis_label_text_font": "Helvetica",
                    "axis_label_text_font_size": "1.25em",
                    "axis_label_text_font_style": "normal",
                },
                "Legend": {
                    "spacing": 8,
                    "glyph_width": 15,
                    "label_standoff": 8,
                    "label_text_color": "#253d8f",
                    "label_text_font": "Helvetica",
                    "label_text_font_size": "1.025em",
                    "border_line_alpha": 0,
                    "background_fill_alpha": 0.45,
                    "background_fill_color": "#e8e8ea",
                },
                "BaseColorBar": {
                    "title_text_color": "#253d8f",
                    "title_text_font": "Helvetica",
                    "title_text_font_size": "1.025em",
                    "title_text_font_style": "normal",
                    "major_label_text_color": "#253d8f",
                    "major_label_text_font": "Helvetica",
                    "major_label_text_font_size": "1.025em",
                    "background_fill_color": "#e8e8ea",
                    "major_tick_line_alpha": 0,
                    "bar_line_alpha": 0,
                },
                "Title": {
                    "text_color": "#253d8f",
                    "text_font": "Helvetica",
                    "text_font_size": "1.15em",
                },
                "Line": {
                    "line_color": "#497bbc",
                },
                "Fill": {
                    "fill_color": "#bf4e30",
                },
                "Text": {
                    "text_color": "#253d8f",
                },
            }
        }
    ),
}

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


class ThemeAccessor:
    """Small accessor around a named collection of Bokeh themes."""

    def __init__(self, default: str = DEFAULT_THEME) -> None:
        """Initialize the accessor with a starting theme.

        Args:
            default: Name of the theme to select initially. Must be a key
                in ``THEMES``.

        Raises:
            ValueError: If `default` is not a key in `THEMES`.
        """
        if default not in THEMES:
            raise ValueError(f"Unknown default theme '{default}'")
        self._name = default

    @property
    def name(self) -> str:
        """Name of the currently selected theme."""
        return self._name

    @property
    def current(self) -> Theme:
        """The currently selected Bokeh `Theme` object."""
        return THEMES[self._name]

    def set(self, name: str) -> None:
        """Switch the active theme and apply it to the current document.

        Args:
            name: Name of the theme to activate. Must be a key in `THEMES`.

        Raises:
            ValueError: If `name` is not a key in `THEMES`.
        """
        if name not in THEMES:
            raise ValueError(f"Unknown theme '{name}'. Options: {list(THEMES)}")
        self._name = name
        curdoc().theme = self.current


# Global accessor for app/notebook code.
theme = ThemeAccessor(default=DEFAULT_THEME)

# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------
