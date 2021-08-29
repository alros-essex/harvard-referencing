from enum import Enum

from harvard.storage import Storage
from harvard.reference import BookReference, Reference, EbookReference, VitalsourceReference
from harvard.collection import Collection

class State(Enum):
    NO_COLLECTIONS = 'No collections'
    CREATE_NEW_COLLECTION = 'Create new collection'
    ACTIVE_COLLECTION = 'Active collection'
    CREATE_NEW_REFERENCE = 'Create new reference'
    LOAD_COLLECTION = 'Load collection'
    EXIT = 'EXIT'

class Utility:
    @staticmethod
    def print_output(data: str):
        print(data)

    @staticmethod
    def prompt_user_for_input(text: str = None, options = None, collection: str = None) -> str:
        while True:
            prompt = '{collection}@harvard § '.format(collection= collection) if text is None else '{text} > '.format(text=text)
            user_input = input(prompt)
            if options is None or user_input in options:
                return user_input if user_input != '' else None
            else:
                print('Err. valid options are {options}'.format(options = options))

class HandlerBase():

    def __init__(self, storage: Storage):
        self.storage = storage

class HandlerNoCollection(HandlerBase):

    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        Utility.print_output('No active collections:')
        Utility.print_output('- Create [N]ew')
        Utility.print_output('- [L]oad collection')
        choice = Utility.prompt_user_for_input(options = ['N','L'])
        return State.CREATE_NEW_COLLECTION if choice == 'N' else State.LOAD_COLLECTION, None
        
class HandlerCreateNewCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        Utility.print_output('Create new collection:')
        name = Utility.prompt_user_for_input(text = 'Input name')
        description = Utility.prompt_user_for_input(text = 'Input description')
        collection = Collection(name = name, description = description)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

class HandlerActiveCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, collection: Collection):
        Utility.print_output('Collection {name}'.format(name = collection.name))
        Utility.print_output('  {description}'.format(description = collection.description))
        Utility.print_output('References')
        if collection.references == []:
            Utility.print_output(' <empty>')
        else:
            for i, reference in enumerate(collection.references):
                Utility.print_output(' [{index}] : {ref}'.format(index = i, ref=reference.format_console()))
        Utility.print_output('Create [N]ew reference')
        user_input = Utility.prompt_user_for_input(options = ['N'])
        return State.CREATE_NEW_REFERENCE if user_input == 'N' else State.EXIT, collection

class HandlerCreateNewReference(HandlerBase):

    def __init__(self,storage: Storage):
        super().__init__(storage)
        self.type_handler = {
            'B': EditBookReference(),
            'E': EditEbookReference(),
            'V': EditVitalsourceReference()
        }

    def handle(self, collection: Collection):
        Utility.print_output('Create new reference')
        Utility.print_output('Type of reference: [B]ook, [E]book, [V]vitalsource')
        user_input = Utility.prompt_user_for_input(options = ['B', 'E', 'V'])
        reference = self.type_handler[user_input].edit()
        collection.add_reference(reference)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

class HandlerLoadCollection(HandlerBase):
    
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        collections = self.storage.list_all_collections()
        Utility.print_output('List of collections:')
        if collections == []:
            Utility.print_output(' <empty>')
            return State.CREATE_NEW_COLLECTION, None
        else:
            options = []
            for i, collection_name in enumerate(collections):
                Utility.print_output(' [{index}] : {name}'.format(index = i, name = collection_name))
                options.append(str(i))
            selected = Utility.prompt_user_for_input(options=options)
            collection = self.storage.find_collection_by_name(collections[int(selected)])
            return State.ACTIVE_COLLECTION, collection

class EditReference():

    def edit(self, reference: Reference):
        values = {}
        values['authors'] = Utility.prompt_user_for_input('Authors ({current})'.format(current = '<empty>' if reference is None else reference.authors))
        values['year'] = Utility.prompt_user_for_input('Year ({current})'.format(current = '<empty>' if reference is None else reference.year))
        values['title'] = Utility.prompt_user_for_input('Title ({current})'.format(current = '<empty>' if reference is None else reference.title))
        return values

class EditBookReference(EditReference):

    def edit(self, reference: BookReference = None):
        values = super().edit(reference)
        values['volume'] = Utility.prompt_user_for_input('Volume ({current})'.format(current = '<empty>' if reference is None else reference.volume))
        values['edition'] = Utility.prompt_user_for_input('Edition ({current})'.format(current = '<empty>' if reference is None else reference.edition))
        values['place'] = Utility.prompt_user_for_input('Place ({current})'.format(current = '<empty>' if reference is None else reference.place))
        values['publisher'] = Utility.prompt_user_for_input('Publisher ({current})'.format(current = '<empty>' if reference is None else reference.publisher))
        return BookReference(
            values['authors'],
            values['year'],
            values['title'],
            values['place'],
            values['publisher'],
            values['volume'],
            values['edition'])

class EditEbookReference(EditReference):

    def edit(self, reference: EbookReference = None):
        values = super().edit(reference)
        values['edition'] = Utility.prompt_user_for_input('Edition ({current})'.format(current = '<empty>' if reference is None else reference.edition))
        values['place'] = Utility.prompt_user_for_input('Place ({current})'.format(current = '<empty>' if reference is None else reference.place))
        values['publisher'] = Utility.prompt_user_for_input('Publisher ({current})'.format(current = '<empty>' if reference is None else reference.publisher))
        values['url'] = Utility.prompt_user_for_input('Url ({current})'.format(current = '<empty>' if reference is None else reference.url))
        values['last_access'] = Utility.prompt_user_for_input('Last accessed ({current})'.format(current = '<empty>' if reference is None else reference.last_access))
        return EbookReference(
            values['authors'],
            values['year'],
            values['title'],
            values['place'],
            values['publisher'],
            values['url'],
            values['last_access'],
            values['edition'])

class EditVitalsourceReference(EditReference):

    def edit(self, reference: VitalsourceReference = None):
        values = super().edit(reference)
        values['edition'] = Utility.prompt_user_for_input('Edition ({current})'.format(current = '<empty>' if reference is None else reference.edition))
        values['place'] = Utility.prompt_user_for_input('Place ({current})'.format(current = '<empty>' if reference is None else reference.place))
        values['publisher'] = Utility.prompt_user_for_input('Publisher ({current})'.format(current = '<empty>' if reference is None else reference.publisher))
        values['last_access'] = Utility.prompt_user_for_input('Last accessed ({current})'.format(current = '<empty>' if reference is None else reference.last_access))
        return VitalsourceReference(
            values['authors'],
            values['year'],
            values['title'],
            values['place'],
            values['publisher'],
            values['last_access'],
            values['edition'])


class Console:

    def __init__(self):
        self.state = State.NO_COLLECTIONS
        self.state_options = None
        self.storage = Storage()
        self.state_handlers = {
            State.NO_COLLECTIONS: HandlerNoCollection(self.storage),
            State.CREATE_NEW_COLLECTION: HandlerCreateNewCollection(self.storage),
            State.ACTIVE_COLLECTION: HandlerActiveCollection(self.storage),
            State.CREATE_NEW_REFERENCE: HandlerCreateNewReference(self.storage),
            State.LOAD_COLLECTION: HandlerLoadCollection(self.storage)
        }

    def loop(self):
        while self.state is not State.EXIT:
            self.state, self.state_options = self.state_handlers[self.state].handle(self.state_options)



def main():
  Console().loop()