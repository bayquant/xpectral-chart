# Xpectral Chart

![Spectral decomposition](https://raw.githubusercontent.com/bayquant/xpectral-chart/main/assets/xpectral_banner.gif)

Fluent Bokeh charting that extends **Polars** and **Pandas** DataFrames via the
accessor pattern: `df.bokeh.line(...)`, `df.bokeh.scatter(...)`, and more.

Part of the Xpectral project, alongside [`xpectral-quant`](https://github.com/bayquant/xpectral-quant)
(financial metrics and market data). Both install into the shared `xpectral`
namespace and can be used together.

## Usage

```python
import xpectral.charts  # registers the df.bokeh accessor
from xpectral.charts import PandasDataFrame
from xpectral.charts import PolarsDataFrame

df: PolarsDataFrame = pl.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
fig = df.bokeh(title="Example", width=600, height=400)
fig.line(x="x", y="y")

pd_df: PandasDataFrame = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
pd_fig = pd_df.bokeh(title="Example", width=600, height=400)
pd_fig.line(x="x", y="y")
```

Importing `xpectral.charts` is what registers the accessor on Polars and Pandas
DataFrames. Annotate sample DataFrames with `PolarsDataFrame` or
`PandasDataFrame` when you want the editor (pyright) to resolve the
`df.bokeh(...)` parameters and chained accessor methods — annotation is
necessary for type hinting, as accessors are not discovered dynamically.

### Custom chart methods

Use `BokehAccessor.register` to add your own methods to the accessor. The
decorated function receives `self` — the accessor instance — giving access to
`self._df`, `self.source`, `self.plot`, and all built-in glyph methods.

```python
from xpectral.charts import BokehAccessor

@BokehAccessor.register
def price_band(self, mid, upper, lower, **kwargs):
    self.line(y=mid, **kwargs)
    self.varea(y1=lower, y2=upper, fill_alpha=0.2, **kwargs)

fig = df.bokeh(title="Bands", width=800, height=400)
fig.price_band(mid="close", upper="upper", lower="lower")
```

The method is available on both Polars and Pandas accessors immediately after
registration.

See [`xpectral/charts/README.md`](xpectral/charts/README.md) for the module-level
documentation (glyph methods, stacks, auto-color, themes, datetime axes).

## Install

```bash
pip install xpectral-chart
```

```bash
uv add xpectral-chart
```

For development:

```bash
uv sync
```
