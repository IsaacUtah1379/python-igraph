import abc
from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractEdgeDrawer

__all__ = ['AbstractCairoEdgeDrawer', 'AlphaVaryingEdgeDrawer', 'CairoArrowEdgeDrawer', 'DarkToLightEdgeDrawer', 'LightToDarkEdgeDrawer', 'TaperedEdgeDrawer']

class AbstractCairoEdgeDrawer(AbstractEdgeDrawer, metaclass=abc.ABCMeta):
    context: Incomplete
    palette: Incomplete
    VisualEdgeBuilder: Incomplete
    def __init__(self, context, palette) -> None: ...
    def draw_loop_edge(self, edge, vertex) -> None: ...
    def draw_undirected_edge(self, edge, src_vertex, dest_vertex): ...

class CairoArrowEdgeDrawer(AbstractCairoEdgeDrawer):
    def draw_directed_edge(self, edge, src_vertex, dest_vertex): ...

class TaperedEdgeDrawer(AbstractCairoEdgeDrawer):
    def draw_directed_edge(self, edge, src_vertex, dest_vertex): ...

class AlphaVaryingEdgeDrawer(AbstractCairoEdgeDrawer):
    alpha_at_src: Incomplete
    alpha_at_dest: Incomplete
    def __init__(self, context, palette, alpha_at_src, alpha_at_dest) -> None: ...
    def draw_directed_edge(self, edge, src_vertex, dest_vertex): ...

class LightToDarkEdgeDrawer(AlphaVaryingEdgeDrawer):
    def __init__(self, context, palette) -> None: ...

class DarkToLightEdgeDrawer(AlphaVaryingEdgeDrawer):
    def __init__(self, context, palette) -> None: ...
