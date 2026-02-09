from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractDrawer

__all__ = ['MatplotlibDendrogramDrawer']

class MatplotlibDendrogramDrawer(AbstractDrawer):
    context: Incomplete
    def __init__(self, ax) -> None: ...
    def draw(self, dendro, orientation: str = 'lr', **kwds) -> None: ...
