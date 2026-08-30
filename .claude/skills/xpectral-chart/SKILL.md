---
name: xpectral-chart
description: Use when writing code in THIS repo (xpectral-chart) that plots a Polars/Pandas DataFrame with Bokeh via the df.bokeh accessor — building figures, glyphs, stacked charts, themes, or palettes.
---

# xpectral-chart

Fluent Bokeh charting via a `df.bokeh` accessor on Polars/Pandas DataFrames.
`import xpectral.charts` once to register it; then chain glyph calls.

## Core pattern

```python
import xpectral.charts  # registers df.bokeh, once, top of file

fig = df.bokeh(title="Example", width=600, height=400)  # -> figure, kwargs = bokeh.plotting.figure() options
fig.line(x="x", y="y")          # column names as strings, resolved against df
fig.scatter(x="x", y="y", color="red", size=8)
fig.show()                       # opens in browser / renders in notebook
```

- `df.bokeh(**figure_kwargs)` creates the figure (accepts the same kwargs as
  `bokeh.plotting.figure`: `title`, `width`, `height`, `x_axis_type`, `tools`, etc.).
- Every glyph method (`line`, `scatter`, `vbar`, `varea`, `rect`, `segment`, ...)
  maps 1:1 to a Bokeh glyph — same name, same kwargs — plus one extra:
  `legend: bool = True` (auto-adds a legend entry from the y/x column name).
- Pass column names as strings (`x="date"`); pass a literal array/Series directly
  (not as a string) if the data isn't a column in `df`.
- If `x`/`y` is omitted where required, a 0..n-1 index is auto-injected.
- Color is auto-cycled from a shared palette when no `color`/`*_color` kwarg is
  given — don't hand-pick colors unless the user wants specific ones.
- A `date`/`datetime` column plotted on an axis auto-gets a datetime tick formatter.
- `from xpectral.charts import figure` is a free-function equivalent:
  `figure(df, **kwargs)` instead of `df.bokeh(**kwargs)` — same result, usable
  inline without a typed intermediate variable.

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
from xpectral.charts import BokehAccessor

@BokehAccessor.register
def price_band(self, mid, upper, lower, **kwargs):
    self.line(y=mid, **kwargs)
    self.varea(y1=lower, y2=upper, fill_alpha=0.2, **kwargs)
```
`self` inside a registered function is the accessor: `self._df`, `self.source`
(the `ColumnDataSource`), `self.plot`, and all built-in glyph methods are available.

## Theme / palette (global, process-wide)

```python
from xpectral.charts.theme_manager import theme
theme.set("dark_minimal")  # caliber, carbon, light_minimal (default), dark_minimal, night_sky, contrast, ocean

from xpectral.charts.palette_manager import palette
palette.set(["#1f77b4", "#ff7f0e"])  # replaces the auto-color cycle
```

## Typing (optional, for editor support only)

```python
from xpectral.charts import PolarsDataFrame, PandasDataFrame
df: PolarsDataFrame = pl.DataFrame(...)  # lets pyright resolve df.bokeh(...) params
```

## Reference

Full glyph/kwarg signatures: `xpectral/charts/accessors.pyi`. Figure kwargs:
`figure()` signature in `xpectral/charts/accessors.pyi` (`__call__`). Real usage:
`examples/charts/*.ipynb`, `tests/test__charts_accessors_*.py`.
