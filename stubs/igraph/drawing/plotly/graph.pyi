from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractGraphDrawer

__all__ = ['PlotlyGraphDrawer']

class PlotlyGraphDrawer(AbstractGraphDrawer):
    fig: Incomplete
    vertex_drawer_factory: Incomplete
    edge_drawer_factory: Incomplete
    def __init__(self, fig, vertex_drawer_factory=..., edge_drawer_factory=...) -> None: ...
    def draw(self, graph, *args, **kwds) -> None: ...
