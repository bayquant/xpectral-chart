import unittest

from bokeh.io import curdoc
from bokeh.themes import Theme

from xpectral.charts.theme_manager import DEFAULT_THEME
from xpectral.charts.theme_manager import THEMES
from xpectral.charts.theme_manager import ThemeAccessor
from xpectral.charts.theme_manager import theme


class TestThemeAccessor(unittest.TestCase):
    def test_default_construction(self) -> None:
        accessor = ThemeAccessor()
        self.assertEqual(accessor.name, DEFAULT_THEME)

    def test_construction_with_valid_default(self) -> None:
        accessor = ThemeAccessor(default="ocean")
        self.assertEqual(accessor.name, "ocean")

    def test_construction_with_invalid_default_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown default theme 'bogus'"):
            ThemeAccessor(default="bogus")

    def test_current_returns_theme_instance(self) -> None:
        accessor = ThemeAccessor(default="carbon")
        self.assertIsInstance(accessor.current, Theme)
        self.assertIs(accessor.current, THEMES["carbon"])

    def test_set_valid_name_updates_name_and_current(self) -> None:
        accessor = ThemeAccessor()
        accessor.set("dark_minimal")
        self.assertEqual(accessor.name, "dark_minimal")
        self.assertIs(accessor.current, THEMES["dark_minimal"])

    def test_set_invalid_name_raises(self) -> None:
        accessor = ThemeAccessor()
        with self.assertRaisesRegex(ValueError, "Unknown theme 'bogus'. Options:"):
            accessor.set("bogus")
        self.assertEqual(accessor.name, DEFAULT_THEME)

    def test_set_updates_curdoc_theme(self) -> None:
        accessor = ThemeAccessor()
        accessor.set("night_sky")
        self.assertIs(curdoc().theme, accessor.current)

    def test_module_singleton_default(self) -> None:
        self.assertEqual(theme.name, DEFAULT_THEME)


if __name__ == "__main__":
    unittest.main()
