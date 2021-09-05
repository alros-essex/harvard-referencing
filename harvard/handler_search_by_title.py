from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State

class HandlerSearchCollectionByTitle(HandlerBase):
    
    def __init__(self, storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        # TODO
        pass

    def get_state(self):
        return State.SEARCH_BY_TITLE
