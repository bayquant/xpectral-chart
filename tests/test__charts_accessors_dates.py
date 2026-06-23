from datetime import date
from datetime import datetime
import unittest

import pandas as pd
import polars as pl

from xpectral.charts import accessors


class TestCoerceUnsafeDates(unittest.TestCase):
    def test_polars_date_column_coerced_to_datetime(self) -> None:
        df = pl.DataFrame(
            {
                "x": [date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)],
                "y": [1, 2, 3],
            }
        )
        fig = df.bokeh()
        renderer = fig.line(x="x", y="y")

        values = renderer.data_source.data["x"]
        self.assertTrue(all(isinstance(v, datetime) for v in values))
        self.assertEqual(
            values, [datetime(2026, 1, 1), datetime(2026, 1, 2), datetime(2026, 1, 3)]
        )

    def test_pandas_object_date_column_coerced_to_datetime(self) -> None:
        df = pd.DataFrame(
            {
                "x": [date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)],
                "y": [1, 2, 3],
            }
        )
        self.assertEqual(df["x"].dtype, object)

        fig = df.bokeh()
        renderer = fig.line(x="x", y="y")

        values = renderer.data_source.data["x"]
        self.assertTrue(all(isinstance(v, datetime) for v in values))
        self.assertEqual(
            values, [datetime(2026, 1, 1), datetime(2026, 1, 2), datetime(2026, 1, 3)]
        )

    def test_polars_datetime_column_left_unchanged(self) -> None:
        df = pl.DataFrame(
            {"x": [datetime(2026, 1, 1, 8), datetime(2026, 1, 2, 9)], "y": [1, 2]}
        )
        fig = df.bokeh()
        renderer = fig.line(x="x", y="y")

        self.assertEqual(
            renderer.data_source.data["x"],
            [datetime(2026, 1, 1, 8), datetime(2026, 1, 2, 9)],
        )

    def test_non_date_columns_unaffected(self) -> None:
        df = pl.DataFrame(
            {"x": [1, 2, 3], "y": [1.5, 2.5, 3.5], "label": ["a", "b", "c"]}
        )
        fig = df.bokeh()
        renderer = fig.line(x="x", y="y")

        self.assertEqual(renderer.data_source.data["x"], [1, 2, 3])
        self.assertEqual(renderer.data_source.data["y"], [1.5, 2.5, 3.5])
        self.assertEqual(fig.source.data["label"], ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
