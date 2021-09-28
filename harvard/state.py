from enum import Enum
from enum import Enum

class State(Enum):
    """All possible states of the application"""

    NO_COLLECTIONS = 'NO_COLLECTIONS'
    CREATE_NEW_COLLECTION = 'CREATE_NEW_COLLECTION'
    ACTIVE_COLLECTION = 'ACTIVE_COLLECTION'
    CREATE_NEW_REFERENCE = 'CREATE_NEW_REFERENCE'
    LOAD_COLLECTION = 'LOAD_COLLECTION'
    EDIT_REFERENCE = 'EDIT_REFERENCE'
    DELETE_REFERENCE = 'DELETE_REFERENCE'
    DELETE_COLLECTION = 'DELETE_COLLECTION'
    SEARCH = 'SEARCH'
    SEARCH_BY_AUTHOR = 'SEARCH_BY_AUTHOR'
    SEARCH_BY_TITLE = 'SEARCH_BY_TITLE'
    EXIT = 'EXIT'