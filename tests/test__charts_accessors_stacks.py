from datetime import date
import unittest

import pandas as pd
import polars as pl

from xpectral.charts import accessors


class TestAutoStackers(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pl.DataFrame(
            {
                "step": [0, 1, 2],
                "label": ["a", "b", "c"],
                "d": [date(2024, 1, 1), date(2024, 1, 2), date(2024, 1, 3)],
                "path_0": [1.0, 2.0, 3.0],
                "path_1": [4.0, 5.0, 6.0],
            }
        )

    def test_excludes_non_numeric_and_explicit_coordinate(self) -> None:
        fig = self.df.bokeh()
        renderers = fig.vline_stack(x="step")
        self.assertEqual([r.name for r in renderers], ["path_0", "path_1"])

    def test_explicit_stackers_still_respected(self) -> None:
        fig = self.df.bokeh()
        renderers = fig.vline_stack(x="step", stackers=["path_1", "path_0"])
        self.assertEqual([r.name for r in renderers], ["path_1", "path_0"])

    def test_missing_coordinate_defaults_to_zero_based_range(self) -> None:
        df = pl.DataFrame({"a": [10.0, 20.0, 30.0], "b": [1.0, 2.0, 3.0]})
        fig = df.bokeh()
        renderers = fig.vline_stack()

        self.assertEqual([r.name for r in renderers], ["a", "b"])
        self.assertEqual(fig.source.data["x"], [0, 1, 2])
        self.assertEqual(renderers[0].glyph.x, "x")

    def test_horizontal_family_defaults_and_excludes_y(self) -> None:
        fig = self.df.bokeh()
        renderers = fig.hbar_stack(y="step")
        self.assertEqual([r.name for r in renderers], ["path_0", "path_1"])
        self.assertEqual(renderers[0].glyph.y, "step")

    def test_auto_legend_derives_from_stacker_names(self) -> None:
        fig = self.df.bokeh()
        renderers = fig.vline_stack(x="step")
        legend_labels = [
            r.data_source.data.get("legend_label") or r.glyph.name for r in renderers
        ]
        # legend_label is distributed per-stacker by single_stack; check via the renderer name
        # and that a Legend annotation was created with 2 entries.
        self.assertEqual(len(fig.legend[0].items), 2)
        self.assertEqual(fig.legend[0].items[0].label["value"], "path_0")
        self.assertEqual(fig.legend[0].items[1].label["value"], "path_1")

    def test_legend_false_suppresses_legend(self) -> None:
        fig = self.df.bokeh()
        fig.vline_stack(x="step", legend=False)
        self.assertEqual(len(fig.legend), 0)

    def test_explicit_legend_label_overrides_auto(self) -> None:
        fig = self.df.bokeh()
        fig.vline_stack(x="step", legend_label=["Series A", "Series B"])
        self.assertEqual(fig.legend[0].items[0].label["value"], "Series A")
        self.assertEqual(fig.legend[0].items[1].label["value"], "Series B")

    def test_decorator_auto_legend_from_y_column(self) -> None:
        fig = self.df.bokeh()
        fig.line(x="step", y="path_0")
        self.assertEqual(len(fig.legend[0].items), 1)
        self.assertEqual(fig.legend[0].items[0].label["value"], "path_0")

    def test_decorator_legend_false_suppresses_legend(self) -> None:
        fig = self.df.bokeh()
        fig.line(x="step", y="path_0", legend=False)
        self.assertEqual(len(fig.legend), 0)

    def test_decorator_no_legend_for_synthetic_index(self) -> None:
        df = pl.DataFrame({"path_0": [1.0, 2.0, 3.0]})
        fig = df.bokeh()
        fig.line(y="path_0")
        # x defaults to synthetic "x" column — should still label from y
        self.assertEqual(fig.legend[0].items[0].label["value"], "path_0")

    def test_pandas_auto_stackers_parity(self) -> None:
        df = pd.DataFrame(
            {
                "step": [0, 1, 2],
                "a": [1.0, 2.0, 3.0],
                "b": [4.0, 5.0, 6.0],
                "label": ["x", "y", "z"],
            }
        )
        fig = df.bokeh()
        renderers = fig.vline_stack(x="step")
        self.assertEqual([r.name for r in renderers], ["a", "b"])


if __name__ == "__main__":
    unittest.main()
