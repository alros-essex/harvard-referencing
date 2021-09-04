from harvard.handler_active_collection import HandlerActiveCollection
from harvard.handler_create_collection import HandlerCreateNewCollection
from harvard.handler_create_reference import HandlerCreateNewReference
from harvard.handler_delete_collection import HandlerDeleteCollection
from harvard.handler_delete_reference import HandlerDeleteReference
from harvard.handler_edit_reference import HandlerEditReference
from harvard.handler_load_collection import HandlerLoadCollection
from harvard.handler_no_collection import HandlerNoCollection
from harvard.handler_search import HandlerSearchCollection
from harvard.handler_search_by_author import HandlerSearchCollectionByAuthor
from harvard.handler_search_by_title import HandlerSearchCollectionByTitle
from harvard.storage import Storage
from harvard.state import State

class Console:
    """
    application interface
    """

    def __init__(self):
        self.state = State.NO_COLLECTIONS
        self.state_options = None
        self.storage = Storage()
        self.state_handlers = {
            State.NO_COLLECTIONS: HandlerNoCollection(self.storage),
            State.CREATE_NEW_COLLECTION: HandlerCreateNewCollection(self.storage),
            State.ACTIVE_COLLECTION: HandlerActiveCollection(self.storage),
            State.CREATE_NEW_REFERENCE: HandlerCreateNewReference(self.storage),
            State.LOAD_COLLECTION: HandlerLoadCollection(self.storage),
            State.EDIT_REFERENCE: HandlerEditReference(self.storage),
            State.DELETE_REFERENCE: HandlerDeleteReference(self.storage),
            State.DELETE_COLLECTION: HandlerDeleteCollection(self.storage),
            State.SEARCH: HandlerSearchCollection(self.storage),
            State.SEARCH_BY_AUTHOR: HandlerSearchCollectionByAuthor(self.storage),
            State.SEARCH_BY_TITLE: HandlerSearchCollectionByTitle(self.storage)
        }

    def loop(self):
        """
        main loop of the interface: it delegates the handling to the state-dependent handler
        """
        while self.state is not State.EXIT:
            self.state, self.state_options = self.state_handlers[self.state].handle(self.state_options)

def main():
    """
    entry point: call this method to start the application
    """
    Console().loop()