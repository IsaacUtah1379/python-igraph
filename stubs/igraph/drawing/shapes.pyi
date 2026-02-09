from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['ShapeDrawerDirectory']

class ShapeDrawer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class NullDrawer(ShapeDrawer):
    names: Incomplete
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None) -> None: ...

class RectangleDrawer(ShapeDrawer):
    names: str
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class CircleDrawer(ShapeDrawer):
    names: str
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class UpTriangleDrawer(ShapeDrawer):
    names: str
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class DownTriangleDrawer(ShapeDrawer):
    names: str
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class DiamondDrawer(ShapeDrawer):
    names: str
    @staticmethod
    def draw_path(ctx, center_x, center_y, width, height=None, **kwargs): ...
    @staticmethod
    def intersection_point(center_x, center_y, source_x, source_y, width, height=None): ...

class ShapeDrawerDirectory:
    known_shapes: Incomplete
    @classmethod
    def register(cls, drawer_class) -> None: ...
    @classmethod
    def register_namespace(cls, namespace) -> None: ...
    @classmethod
    def resolve(cls, shape): ...
    @classmethod
    def resolve_default(cls, shape, default=...): ...
