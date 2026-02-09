from _typeshed import Incomplete
from igraph.drawing.cairo.graph import CairoGraphDrawer as CairoGraphDrawer
from igraph.drawing.cairo.plot import CairoPlot
from igraph.drawing.matplotlib.graph import MatplotlibGraphDrawer as MatplotlibGraphDrawer
from igraph.drawing.utils import BoundingBox as BoundingBox, Point as Point, Rectangle as Rectangle

__all__ = ['BoundingBox', 'CairoGraphDrawer', 'MatplotlibGraphDrawer', 'DefaultGraphDrawer', 'Plot', 'Point', 'Rectangle', 'plot', 'DrawerDirectory']

Plot = CairoPlot
DefaultGraphDrawer = CairoGraphDrawer

class DrawerDirectory:
    valid_backends: Incomplete
    valid_objects: Incomplete
    known_drawers: Incomplete
    @classmethod
    def resolve(cls, obj, backend): ...

def plot(obj, target=None, bbox=(0, 0, 600, 600), *args, **kwds): ...
