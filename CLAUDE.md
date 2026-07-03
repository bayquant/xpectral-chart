# CLAUDE.md

## Xpectral Chart

Fluent Bokeh charting that extends **Pandas** and **Polars** DataFrames with a
`df.bokeh` accessor, registered via Python's accessor registration pattern.

`xpectral` is a PEP 420 namespace package shared with the separate
[`xpectral-quant`](https://github.com/bayquant/xpectral-quant) project — there is
no top-level `xpectral/__init__.py`. Importing `xpectral.charts` is what
registers the accessor.

The charts subpackage documents its own modules:

- [`xpectral/charts/README.md`](xpectral/charts/README.md)
