import abc
from .base import AbstractCairoDrawer
from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractVertexDrawer

__all__ = ['AbstractCairoVertexDrawer', 'CairoVertexDrawer']

class AbstractCairoVertexDrawer(AbstractVertexDrawer, AbstractCairoDrawer, metaclass=abc.ABCMeta):
    def __init__(self, context, bbox, palette, layout) -> None: ...

class CairoVertexDrawer(AbstractCairoVertexDrawer):
    VisualVertexBuilder: Incomplete
    def __init__(self, context, bbox, palette, layout) -> None: ...
    def draw(self, visual_vertex, vertex, coords) -> None: ...
