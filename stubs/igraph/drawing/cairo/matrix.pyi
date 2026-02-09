from igraph.drawing.cairo.base import AbstractCairoDrawer

__all__ = ['CairoMatrixDrawer']

class CairoMatrixDrawer(AbstractCairoDrawer):
    def __init__(self, context) -> None: ...
    def draw(self, matrix, **kwds) -> None: ...
