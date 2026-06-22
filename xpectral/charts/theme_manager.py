"""Central theme management for Bokeh apps."""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations
from typing import Any

# Other imports
from bokeh.io import curdoc
from bokeh.themes import built_in_themes
from bokeh.themes import Theme

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

DEFAULT_THEME = "light_minimal"

# Structural/UX defaults merged into every theme below (built-in and custom).
# Kept intentionally free of colors/fonts so it never overrides a theme's own
# visual identity — add more cross-theme defaults here as the need arises.
BASE_ATTRS: dict[str, dict[str, Any]] = {
    "Toolbar": {
        "logo": None,
        "autohide": True,
    },
}

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
                "Plot": {
                    "background_fill_color": "#f3f6fa",
                    "border_fill_color": "#f3f6fa",
                    "outline_line_color": "#1c2f5e",
                    "outline_line_alpha": 0.4,
                    "min_border_left": 36,
                    "min_border_right": 24,
                    "min_border_top": 26,
                    "min_border_bottom": 36,
                },
                "Grid": {
                    "grid_line_color": "#9fb3d1",
                    "grid_line_alpha": 0.18,
                },
                "Axis": {
                    "major_tick_line_alpha": 0.45,
                    "major_tick_line_color": "#3c5a96",
                    "minor_tick_line_alpha": 0.3,
                    "minor_tick_line_color": "#3c5a96",
                    "axis_line_alpha": 0.6,
                    "axis_line_color": "#1c2f5e",
                    "major_label_text_color": "#34466b",
                    "major_label_text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "major_label_text_font_size": "1.025em",
                    "axis_label_standoff": 5,
                    "axis_label_text_color": "#1c2f5e",
                    "axis_label_text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "axis_label_text_font_size": "1.25em",
                    "axis_label_text_font_style": "normal",
                },
                "Legend": {
                    "spacing": 8,
                    "glyph_width": 15,
                    "label_standoff": 8,
                    "label_text_color": "#1c2f5e",
                    "label_text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "label_text_font_size": "1.025em",
                    "border_line_alpha": 0.2,
                    "border_line_color": "#1c2f5e",
                    "background_fill_alpha": 0.6,
                    "background_fill_color": "#f3f6fa",
                },
                "BaseColorBar": {
                    "title_text_color": "#1c2f5e",
                    "title_text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "title_text_font_size": "1.025em",
                    "title_text_font_style": "normal",
                    "major_label_text_color": "#1c2f5e",
                    "major_label_text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "major_label_text_font_size": "1.025em",
                    "background_fill_color": "#f3f6fa",
                    "major_tick_line_alpha": 0,
                    "bar_line_alpha": 0.3,
                    "bar_line_color": "#1c2f5e",
                },
                "Title": {
                    "text_color": "#1c2f5e",
                    "text_font": "Helvetica Neue, Helvetica, Arial, sans-serif",
                    "text_font_size": "1.15em",
                },
                "Line": {
                    "line_color": "#2e6da4",
                },
                "Fill": {
                    "fill_color": "#e2654b",
                },
                "Text": {
                    "text_color": "#1c2f5e",
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


def register_theme(name: str, attrs: dict[str, dict[str, Any]]) -> Theme:
    """Register a custom theme and add it to `THEMES`.

    Args:
        name: Key to register the theme under. Must not already be a key
            in `THEMES`.
        attrs: Bokeh theme `attrs` mapping (model class name -> dict of
            property overrides), the same shape passed to
            ``Theme(json={"attrs": ...})``. Merged on top of `BASE_ATTRS`
            so the new theme automatically inherits the shared toolbar
            defaults; entries in `attrs` win on conflicts.

    Returns:
        The constructed `Theme`, already added to `THEMES` under `name`.

    Raises:
        ValueError: If `name` is already a key in `THEMES`.
    """
    if name in THEMES:
        raise ValueError(
            f"Theme '{name}' is already registered. Options: {list(THEMES)}"
        )
    new_theme = Theme(json={"attrs": _merge_attrs(BASE_ATTRS, attrs)})
    THEMES[name] = new_theme
    return new_theme


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------


def _merge_attrs(
    base: dict[str, dict[str, Any]], override: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    # Shallow-merge two Bokeh theme `attrs` dicts (class name -> prop dict);
    # `override` wins per-property, matching Theme._for_class's own
    # base-then-subclass merge order.
    merged = {class_name: dict(props) for class_name, props in base.items()}
    for class_name, props in override.items():
        merged.setdefault(class_name, {}).update(props)
    return merged


def _attrs_of(theme: Theme) -> dict[str, dict[str, Any]]:
    # Theme has no public getter for the attrs it was built with; this is
    # the only place that reaches into Bokeh's private `_json` field (see
    # bokeh.themes.theme.Theme.__init__, which stores the constructor's
    # `json` arg verbatim as `self._json`).
    return theme._json.get("attrs", {})


for _name, _theme in THEMES.items():
    THEMES[_name] = Theme(json={"attrs": _merge_attrs(BASE_ATTRS, _attrs_of(_theme))})
