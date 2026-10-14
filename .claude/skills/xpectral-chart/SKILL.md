---
name: xpectral-chart
description: Use when writing code in THIS repo (xpectral-chart) that plots a Polars/Pandas DataFrame with Bokeh via the figure() function: building figures, glyphs, stacked charts, themes, or palettes.
---

# xpectral-chart

Fluent Bokeh charting via the `figure()` function on Polars/Pandas DataFrames.

## Core pattern

```python
from xpectral_chart import figure

fig = figure(df, title="Example", width=600, height=400)  # kwargs = bokeh.plotting.figure() options
fig.line(x="x", y="y")          # column names as strings, resolved against df
fig.scatter(x="x", y="y", color="red", size=8)
fig.show()                       # opens in browser / renders in notebook
```

- `figure(df, **figure_kwargs)` creates the figure (accepts the same kwargs as
  `bokeh.plotting.figure`: `title`, `width`, `height`, `x_axis_type`, `tools`, etc.),
  fully typed: no annotation needed for editor support.
- Every glyph method (`line`, `scatter`, `vbar`, `varea`, `rect`, `segment`, ...)
  maps 1:1 to a Bokeh glyph (same name, same kwargs) plus one extra:
  `auto_legend: bool = True` (auto-adds a legend entry from the y/x column name;
  distinct from Bokeh's own `legend=` kwarg, which attaches an existing Legend/field).
- Pass column names as strings (`x="date"`); pass a literal array/Series directly
  (not as a string) if the data isn't a column in `df`.
- If `x`/`y` is omitted where required, a 0..n-1 index is auto-injected.
- Color is auto-cycled from a shared palette when no `color`/`*_color` kwarg is
  given. Don't hand-pick colors unless the user wants specific ones.
- A `date`/`datetime` column plotted on an axis auto-gets a datetime tick formatter.

## Stacked charts

`vbar_stack`, `hbar_stack`, `varea_stack`, `harea_stack`, `vline_stack`, `hline_stack`:

```python
fig.vbar_stack(["a", "b", "c"], x="date", width=0.8)  # stackers cumulate bottom-to-top
fig.vline_stack()  # stackers=None -> every numeric column except x/y is stacked
```

`x` (vertical stacks) or `y` (horizontal stacks) is the shared coordinate;
each stacker column becomes one glyph renderer, auto-legended by column name.

## Custom methods

```python
from xpectral_chart import BokehAccessor

@BokehAccessor.register
def price_band(self, mid, upper, lower, **kwargs):
    self.line(y=mid, **kwargs)
    self.varea(y1=lower, y2=upper, fill_alpha=0.2, **kwargs)
```
`self` inside a registered function is the accessor: `self._df`, `self.source`
(the `ColumnDataSource`), `self.plot`, and all built-in glyph methods are available.

## Theme / palette (global, process-wide)

```python
from xpectral_chart.theme_manager import theme
theme.set("dark_minimal")  # caliber, carbon, light_minimal (default), dark_minimal, night_sky, contrast, ocean

from xpectral_chart.palette_manager import palette
palette.set(["#1f77b4", "#ff7f0e"])  # replaces the auto-color cycle
```

## Reference

Full glyph/kwarg signatures: `xpectral_chart/accessors.pyi`. Figure kwargs:
`figure()` signature in `xpectral_chart/__init__.py`. Real usage:
`examples/charts/*.ipynb`, `tests/test__charts_accessors_*.py`.
