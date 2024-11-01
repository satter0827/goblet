from enum import IntEnum, Enum, auto

BOARD_SIZE = 3

NUM_OF_SMALL_PIECES = 3
NUM_OF_MIDDLE_PIECES = 3
NUM_OF_LARGE_PIECES = 3

NONE_ID = 0

PLAYER_ID = {
    "first": 1,
    "second": 2,
}

STONE_ID = {
    "small": 1,
    "middle": 2,
    "large": 3,
}

class Stone_Size(Enum):
    SMALL = auto()
    MIDDLE = auto()
    LARGE = auto()

class Matrix(IntEnum):
    ROW = 3
    COL = 3

class Stone(Enum):
    ON = auto()
    OFF = auto()