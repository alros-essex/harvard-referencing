from harvard.handler_base import HandlerBase
from harvard.storage import Storage

class HandlerSearchCollectionByTitle(HandlerBase):
    
    def __init__(self, storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        # TODO
        pass