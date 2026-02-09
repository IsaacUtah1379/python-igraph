from .base import AbstractCairoDrawer
from _typeshed import Incomplete

__all__ = ['CairoDendrogramDrawer']

class CairoDendrogramDrawer(AbstractCairoDrawer):
    palette: Incomplete
    def __init__(self, context, bbox, palette) -> None: ...
    def draw(self, dendro, **kwds) -> None: ...
