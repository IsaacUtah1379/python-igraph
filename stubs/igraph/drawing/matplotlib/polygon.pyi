from igraph.drawing.utils import FakeModule

__all__ = ['HullCollection']

PathCollection = FakeModule

class HullCollection(PathCollection):
    def __init__(self, *args, **kwargs) -> None: ...
    def draw(self, renderer): ...
