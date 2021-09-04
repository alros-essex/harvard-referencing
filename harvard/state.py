from enum import Enum
from enum import Enum, auto

class State(Enum):
    """
    all possible states of the application
    """

    NO_COLLECTIONS = auto()
    CREATE_NEW_COLLECTION = auto()
    ACTIVE_COLLECTION = auto()
    CREATE_NEW_REFERENCE = auto()
    LOAD_COLLECTION = auto()
    EDIT_REFERENCE = auto()
    DELETE_REFERENCE = auto()
    DELETE_COLLECTION = auto()
    SEARCH = auto()
    SEARCH_BY_AUTHOR = auto()
    SEARCH_BY_TITLE = auto()
    EXIT = auto()