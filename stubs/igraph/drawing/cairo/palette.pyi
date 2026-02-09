from igraph.drawing.cairo.base import AbstractCairoDrawer

__all__ = ['CairoPaletteDrawer']

class CairoPaletteDrawer(AbstractCairoDrawer):
    def __init__(self, context) -> None: ...
    def draw(self, palette, **kwds): ...
