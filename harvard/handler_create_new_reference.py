from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.edit_reference import *
from harvard.state import State
from harvard.utility import Utility

class HandlerCreateNewReference(HandlerBase):

    def __init__(self,storage: Storage):
        super().__init__(storage)
        self.type_handler = {
            'B': EditBookReference(),
            'E': EditEbookReference(),
            'V': EditVitalsourceReference()
        }

    def handle(self, collection: Collection):
        Utility.print_lines([
            '@title Create new reference',
            '@option [B]ook',
            '@option [E]book',
            '@option [V]vitalsource'
        ])
        user_input = Utility.prompt_user_for_input(options = ['B', 'E', 'V'])
        reference = self.type_handler[user_input].edit()
        collection.add_reference(reference)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection