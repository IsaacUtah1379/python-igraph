from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractVertexDrawer

__all__ = ['PlotlyVerticesDrawer']

class PlotlyVerticesDrawer(AbstractVertexDrawer):
    fig: Incomplete
    VisualVertexBuilder: Incomplete
    def __init__(self, fig, palette, layout) -> None: ...
    def draw(self, visual_vertex, vertex, point) -> None: ...
    def draw_label(self, visual_vertex, point, **kwds) -> None: ...
