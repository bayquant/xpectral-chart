# `xpectral.charts`

Fluent Bokeh charting via Pandas/Polars DataFrame accessors (`df.bokeh(...)`).

See the [project README](../../README.md#xpectralcharts) for usage and the custom-method registration example, and [`examples/charts`](../../examples/charts) for runnable notebooks.

## Modules

- **`accessors.py`** — `BokehAccessor` (`Figure` subclass) plus the `PolarsBokehAccessor` and `PandasBokehAccessor` registered under `df.bokeh`. `BokehAccessor.register` attaches new chart methods to all three. Both accessors' `source` property coerces bare `datetime.date` values (Polars `Date` columns, or pandas `object`-dtype columns of raw dates) to `datetime.datetime` before building the `ColumnDataSource`, since Bokeh serializes bare dates as strings rather than numeric timestamps, which breaks glyph positioning.
- **`_figure.py`** — Figure construction backing the accessor.
- **`_decorators.py`** — `glyph_method`, which wraps Bokeh glyph classes into accessor methods with validated signatures and synthesized docstrings.
- **`theme_manager.py`** — `theme.set(name)` to switch the active Bokeh theme. Built-in Bokeh themes (`caliber`, `carbon`, `light_minimal`, `dark_minimal`, `night_sky`, `contrast`) plus a custom `ocean` theme; defaults to `light_minimal`. All themes share `BASE_ATTRS` (toolbar logo/autohide); `register_theme(name, attrs)` adds a custom theme that inherits those defaults.
