from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerCreateNewCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        Utility.print_lines([
            '',
            '@title Create new collection:',
            ''])
        name = Utility.prompt_user_for_input(text = 'Input name')
        description = Utility.prompt_user_for_input(text = 'Input description')
        collection = Collection(name = name, description = description)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.CREATE_NEW_COLLECTION
