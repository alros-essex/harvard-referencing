from harvard.handler_base import HandlerBase
from harvard.state import State
from harvard.utility import Utility
from harvard.reference import ReferenceType
from harvard.edit_reference import *

class HandlerEditReference(HandlerBase):

    def __init__(self, storage):
        super().__init__(storage)
        self.type_handler = {
            ReferenceType.BOOK: EditBookReference(),
            ReferenceType.EBOOK: EditEbookReference(),
            ReferenceType.VITALSOURCE: EditVitalsourceReference()
        }

    def handle(self, data):
        options = data['options']
        collection = data['collection']
        selection = Utility.prompt_user_for_input(text = 'select the index of the reference', options = list(map(str,options)))
        reference = collection.references[int(selection)]
        Utility.print_lines([
            '',
            '@title Editing',
            ' {ref}'.format(ref = reference.format_console()),
            ''
        ])
        reference = self.type_handler[reference.type].edit(reference)
        collection.references[int(selection)] = reference
        return State.ACTIVE_COLLECTION, collection