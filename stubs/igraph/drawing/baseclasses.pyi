import abc
from .text import TextAlignment as TextAlignment
from .utils import evaluate_cubic_bezier as evaluate_cubic_bezier, get_bezier_control_points_for_curved_edge as get_bezier_control_points_for_curved_edge
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class AbstractDrawer(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, *args, **kwds): ...

class AbstractXMLRPCDrawer(AbstractDrawer, metaclass=abc.ABCMeta):
    server: Incomplete
    service: Incomplete
    def __init__(self, url, service=None) -> None: ...

class AbstractEdgeDrawer(metaclass=ABCMeta):
    @abstractmethod
    def draw_directed_edge(self, edge, src_vertex, dest_vertex): ...
    @abstractmethod
    def draw_undirected_edge(self, edge, src_vertex, dest_vertex): ...
    def get_label_position(self, edge, src_vertex, dest_vertex): ...
    def get_label_rotation(self, edge, src_vertex, dest_vertex): ...

class AbstractVertexDrawer(AbstractDrawer, metaclass=abc.ABCMeta):
    layout: Incomplete
    palette: Incomplete
    def __init__(self, palette, layout) -> None: ...
    @abstractmethod
    def draw(self, visual_vertex, vertex, coords): ...

class AbstractGraphDrawer(AbstractDrawer, metaclass=abc.ABCMeta):
    @abstractmethod
    def draw(self, graph, *args, **kwds): ...
    @staticmethod
    def ensure_layout(layout, graph=None): ...
