from enum import Enum, auto


class State(Enum):
    DIAGNOSTIC = auto()
    ATTRACT = auto()
    PLAYING = auto()
    PAUSED = auto()
    MENU = auto()
    HIGH_SCORE = auto()
