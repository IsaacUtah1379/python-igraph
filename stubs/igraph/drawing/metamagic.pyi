from _typeshed import Incomplete

__all__ = ['AttributeSpecification', 'AttributeCollectorBase']

class AttributeSpecification:
    name: Incomplete
    default: Incomplete
    alt_name: Incomplete
    transform: Incomplete
    func: Incomplete
    accessor: Incomplete
    def __init__(self, name, default=None, alt_name=None, transform=None, func=None) -> None: ...

class AttributeCollectorMeta(type):
    def __new__(mcs, name, bases, attrs): ...
    @classmethod
    def record_generator(cls, name, slots): ...

class AttributeCollectorBase(metaclass=AttributeCollectorMeta):
    seq: Incomplete
    kwds: Incomplete
    def __init__(self, seq, kwds=None) -> None: ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
