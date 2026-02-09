from contextlib import contextmanager
from typing import Iterator

__all__ = ['safe_locale']

@contextmanager
def safe_locale() -> Iterator[None]: ...
