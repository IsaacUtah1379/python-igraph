from _typeshed import Incomplete

__all__ = ['GraphSummary', 'summary']

class FakeWrapper:
    def __init__(self, *args, **kwds) -> None: ...
    def fill(self, text): ...
    def wrap(self, text): ...

class GraphSummary:
    edge_list_format: Incomplete
    max_rows: Incomplete
    print_graph_attributes: Incomplete
    print_vertex_attributes: Incomplete
    print_edge_attributes: Incomplete
    verbosity: Incomplete
    width: Incomplete
    wrapper: Incomplete
    def __init__(self, graph, verbosity: int = 0, width: int = 78, edge_list_format: str = 'auto', max_rows: int = 99999, print_graph_attributes: bool = False, print_vertex_attributes: bool = False, print_edge_attributes: bool = False, full: bool = False) -> None: ...

def summary(obj, stream=None, *args, **kwds) -> None: ...
