from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractDrawer

__all__ = ['MatplotlibHistogramDrawer']

class MatplotlibHistogramDrawer(AbstractDrawer):
    context: Incomplete
    def __init__(self, ax) -> None: ...
    def draw(self, matrix, **kwds) -> None: ...
