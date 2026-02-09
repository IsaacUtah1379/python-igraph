import abc
from _typeshed import Incomplete
from igraph.drawing.baseclasses import AbstractDrawer
from igraph.drawing.utils import BoundingBox

__all__ = ['AbstractCairoDrawer']

class AbstractCairoDrawer(AbstractDrawer, metaclass=abc.ABCMeta):
    context: Incomplete
    def __init__(self, context, bbox: None) -> None: ...
    @property
    def bbox(self) -> BoundingBox: ...
    @bbox.setter
    def bbox(self, bbox) -> None: ...
