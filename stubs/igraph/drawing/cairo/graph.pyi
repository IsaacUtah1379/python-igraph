import abc
from .base import AbstractCairoDrawer
from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractGraphDrawer

__all__ = ['CairoGraphDrawer']

class AbstractCairoGraphDrawer(AbstractGraphDrawer, AbstractCairoDrawer, metaclass=abc.ABCMeta):
    def __init__(self, context, bbox) -> None: ...

class CairoGraphDrawer(AbstractCairoGraphDrawer):
    vertex_drawer_factory: Incomplete
    edge_drawer_factory: Incomplete
    label_drawer_factory: Incomplete
    def __init__(self, context, bbox=None, vertex_drawer_factory=..., edge_drawer_factory=..., label_drawer_factory=...) -> None: ...
    bbox: Incomplete
    def draw(self, graph, *args, **kwds) -> None: ...
