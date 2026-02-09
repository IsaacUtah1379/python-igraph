from igraph.drawing.cairo.base import AbstractCairoDrawer

__all__ = ['CairoHistogramDrawer']

class CairoHistogramDrawer(AbstractCairoDrawer):
    def __init__(self, context) -> None: ...
    def draw(self, histogram, **kwds) -> None: ...
