from enum import Enum

class TransferStatus(Enum):
    OK=0
    ERROR=1
    BREAK=2
    NO_FACE=3