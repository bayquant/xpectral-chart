"""Central palette management for automatic per-series glyph colors."""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from __future__ import annotations
from typing import Sequence

# Other imports
from bokeh.palettes import Category10

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

__all__ = ["PaletteAccessor", "palette"]

# Category10's ten colors are the same tab10 set matplotlib/pandas cycle
# through per series, so this default matches pandas.DataFrame.plot().
DEFAULT_PALETTE: tuple[str, ...] = Category10[10]

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


class PaletteAccessor:
    """Settable, cycling palette used for automatic per-series colors.

    Mirrors the global :class:`~xpectral.charts.theme_manager.ThemeAccessor`
    pattern: a module-level ``palette`` instance whose colors drive the
    auto-color assigned to glyphs that leave their color unset. Themes still
    control everything else (axes, grid, fonts, backgrounds).
    """

    def __init__(self, colors: Sequence[str] = DEFAULT_PALETTE) -> None:
        """Initialize the accessor with a starting list of colors.

        Args:
            colors: Ordered sequence of color values to cycle through. Any
                Bokeh palette works (e.g. ``Category20[20]``), as does a plain
                list of CSS/hex strings.
        """
        self._colors = tuple(colors)

    @property
    def colors(self) -> tuple[str, ...]:
        """The colors currently cycled through, in order."""
        return self._colors

    def color(self, index: int) -> str:
        """Return the color at `index`, wrapping past the end of the palette.

        Args:
            index: Zero-based series position. Values at or beyond the palette
                length wrap around, so the palette never runs out.

        Returns:
            A single color value from the palette.
        """
        return self._colors[index % len(self._colors)]

    def set(self, colors: Sequence[str]) -> None:
        """Replace the active palette.

        Args:
            colors: Ordered sequence of color values to cycle through. Any
                Bokeh palette (e.g. ``Category20[20]``) or a plain list of
                CSS/hex strings.

        Raises:
            ValueError: If `colors` is empty.
        """
        colors = tuple(colors)
        if not colors:
            raise ValueError("palette must contain at least one color")
        self._colors = colors


# Global accessor for app/notebook code.
palette = PaletteAccessor()


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------
