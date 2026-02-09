from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from igraph import __version__ as __version__
from igraph._igraph import set_progress_handler as set_progress_handler, set_status_handler as set_status_handler
from igraph.configuration import Configuration as Configuration

class TerminalController:
    BOL: str
    UP: str
    DOWN: str
    LEFT: str
    RIGHT: str
    CLEAR_SCREEN: str
    CLEAR_EOL: str
    CLEAR_BOL: str
    CLEAR_EOS: str
    BOLD: str
    BLINK: str
    DIM: str
    REVERSE: str
    NORMAL: str
    HIDE_CURSOR: str
    SHOW_CURSOR: str
    BLACK: str
    BLUE: str
    GREEN: str
    CYAN: str
    RED: str
    MAGENTA: str
    YELLOW: str
    WHITE: str
    BG_BLACK: str
    BG_BLUE: str
    BG_GREEN: str
    BG_CYAN: str
    BG_RED: str
    BG_MAGENTA: str
    BG_YELLOW: str
    BG_WHITE: str
    COLS: Incomplete
    LINES: Incomplete
    def __init__(self, term_stream=...) -> None: ...
    def render(self, template): ...

class ProgressBar:
    BAR: str
    HEADER: str
    term: Incomplete
    width: Incomplete
    progress_bar: Incomplete
    header: Incomplete
    cleared: bool
    last_percent: int
    last_message: str
    def __init__(self, term) -> None: ...
    def update(self, percent=None, message=None) -> None: ...
    def update_message(self, message): ...
    def clear(self) -> None: ...

class Shell(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self): ...
    def supports_progress_bar(self): ...
    def supports_status_messages(self): ...
    def get_progress_handler(self): ...
    def get_status_handler(self): ...

class IDLEShell(Shell):
    def __init__(self) -> None: ...
    def __call__(self) -> None: ...

class ConsoleProgressBarMixin:
    def __init__(self) -> None: ...

class IPythonShell(Shell, ConsoleProgressBarMixin):
    ipython_version: Incomplete
    def __init__(self) -> None: ...
    def __call__(self) -> None: ...

class ClassicPythonShell(Shell, ConsoleProgressBarMixin):
    def __init__(self) -> None: ...
    def __call__(self) -> None: ...

def main() -> None: ...
