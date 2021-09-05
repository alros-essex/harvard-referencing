from harvard.handler_base import HandlerBase
from harvard.state import State
from harvard.utility import Utility

class HandlerDeleteReference(HandlerBase):

    def __init__(self, storage):
        super().__init__(storage)
    
    def handle(self, data):
        options = data['options']
        collection = data['collection']
        selection = Utility.prompt_user_for_input(text='index to delete', options = list(map(str,options)))
        collection.references.pop(int(selection))
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.DELETE_REFERENCE
