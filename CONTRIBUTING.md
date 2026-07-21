# Contributing

## Setup

```bash
uv sync --group dev
uv run pre-commit install
```

`pre-commit install` registers the git hook that applies the repo's formatter locally before you commit.

## Environment Configuration

No external dependencies requiring env config (bokeh, pandas, polars, and pyarrow have no credential requirements).
