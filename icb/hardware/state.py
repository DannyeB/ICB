from enum import Enum, auto


class State(Enum):
    DIAGNOSTIC = auto()
    IDLE = auto()
    RUNNING = auto()
    MENU = auto()
    HIGHSCORE = auto()
