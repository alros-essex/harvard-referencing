from enum import Enum

class State(Enum):
    NO_COLLECTIONS = 'No collections'
    CREATE_NEW_COLLECTION = 'Create new collection'
    ACTIVE_COLLECTION = 'Active collection'
    CREATE_NEW_REFERENCE = 'Create new reference'
    LOAD_COLLECTION = 'Load collection'
    EDIT_REFERENCE = 'Edit reference'
    DELETE_REFERENCE = 'Delete reference'
    DELETE_COLLECTION = 'Delete collection'
    SEARCH = 'Search'
    SEARCH_BY_AUTHOR = 'Search by author'
    SEARCH_BY_TITLE = 'Search by title'
    EXIT = 'EXIT'