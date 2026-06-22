import unittest

from bokeh.io import curdoc
from bokeh.models import Plot
from bokeh.models import Toolbar
from bokeh.models.glyphs import Line
from bokeh.themes import built_in_themes
from bokeh.themes import Theme

from xpectral.charts.theme_manager import DEFAULT_THEME
from xpectral.charts.theme_manager import register_theme
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


class TestThemeDefaultsAndRegistration(unittest.TestCase):
    def test_base_attrs_applied_to_builtin_theme(self) -> None:
        toolbar = Toolbar()
        THEMES["caliber"].apply_to_model(toolbar)
        self.assertIsNone(toolbar.logo)
        self.assertTrue(toolbar.autohide)

    def test_base_attrs_do_not_override_theme_specific_values(self) -> None:
        plot_unmerged = Plot()
        plot_merged = Plot()
        built_in_themes["caliber"].apply_to_model(plot_unmerged)
        THEMES["caliber"].apply_to_model(plot_merged)
        self.assertEqual(
            plot_unmerged.background_fill_color, plot_merged.background_fill_color
        )

    def test_register_theme_adds_and_is_selectable(self) -> None:
        register_theme("mint", {"Line": {"line_color": "#2ecc71"}})

        accessor = ThemeAccessor()
        accessor.set("mint")
        self.assertEqual(accessor.name, "mint")

        line = Line()
        toolbar = Toolbar()
        THEMES["mint"].apply_to_model(line)
        THEMES["mint"].apply_to_model(toolbar)
        self.assertEqual(line.line_color, "#2ecc71")
        self.assertIsNone(toolbar.logo)
        self.assertTrue(toolbar.autohide)

    def test_register_theme_duplicate_name_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, "already registered"):
            register_theme(DEFAULT_THEME, {})


if __name__ == "__main__":
    unittest.main()
