# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Local imports
from .accessors import BokehAccessor

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

__all__ = [
    "BokehAccessor",
    "figure",
]

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------


def figure(df, **kwargs):
    """Create a Bokeh figure from a Polars or Pandas DataFrame.

    Args:
        df: A Polars or Pandas DataFrame.

    Returns:
        A :class:`~xpectral_chart.BokehAccessor` bound to ``df``, ready for
        glyph calls (e.g. :meth:`~BokehAccessor.vline_stack`, :meth:`~BokehAccessor.line`).

    Example::

        fig = figure(df.drop("step"), title="My chart", width=700)
        fig.vline_stack(color=Sunset10)
        fig.show()
    """
    return BokehAccessor(df)(**kwargs)


# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------
