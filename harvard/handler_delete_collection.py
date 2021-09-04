from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerDeleteCollection(HandlerBase):
    
    def __init__(self, storage: Storage):
        super().__init__(storage)

    def handle(self, collection:Collection):
        Utility.print_lines([
            '',
            '@warning Do you want to delete collection?',
            ''
            ])
        choice = Utility.prompt_user_for_input(options=['Y','N'])
        if choice == 'Y':
            self.storage.delete_collection(collection)
            return State.NO_COLLECTIONS, None
        else:
            return State.ACTIVE_COLLECTION, collection