from enum import Enum, auto


class State(Enum):
    DIAGNOSTIC = auto()
    ATTRACT = auto()
    PLAYING = auto()
    PAUSED = auto()
    MENU = auto()
    HIGH_SCORE = auto()
    HOMING = auto()
    HOMED = auto()
    STAGE_COMPLETE = auto()
    GAME_OVER = auto()
    ENTER_HIGH_SCORE = auto()
