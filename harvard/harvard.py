import abc
import enum
from colorama import Fore, Back, Style
from enum import Enum

from harvard.collection import Collection
from harvard.reference import BookReference, EbookReference, Reference, ReferenceType, VitalsourceReference
from harvard.storage import Storage

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

class Utility:
    
    @staticmethod
    def print_lines(lines: list):
        for line in lines:
            if isinstance(line, list):
                Utility.print_lines(line)
            else:
                if line.startswith('@title'):
                    line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                        color_fg = Fore.BLACK, color_bg = Back.WHITE, reset_bg = Back.RESET, reset_fg = Fore.RESET)
                elif line.startswith('@subtitle'):
                    line = '{style}{line}{reset_st}'.format(line = line[len('@subtitle'):],style = Style.DIM, reset_st = Style.RESET_ALL)
                elif line.startswith('@option'):
                    line = '{style} - {line}{reset_st}'.format(line = line[len('@option'):],style = Style.DIM, reset_st = Style.RESET_ALL)
                elif line.startswith('@warning'):
                    line = '{color_fg}{color_bg}{line}{reset_bg}{reset_fg}'.format(line = line[len('@title'):],
                        color_fg = Fore.YELLOW, color_bg = Back.RED, reset_bg = Back.RESET, reset_fg = Fore.RESET)
                print(line)

    @staticmethod
    def prompt_user_for_input(text: str = None, options = None) -> str:
        while True:
            user_input = input('{prompt} > '.format(prompt = text if text is not None else options if options is not None else ''))
            if options is None or user_input in options:
                return user_input if user_input != '' else None
            else:
                print('{color}Err. valid options are {options}{reset_fore}'.format(
                    color=Fore.RED, options = options, reset_fore = Fore.RESET))

class HandlerBase():

    def __init__(self, storage: Storage):
        self.storage = storage

    @abc.abstractmethod
    def handle(self, option):
        pass

class HandlerNoCollection(HandlerBase):

    def __init__(self,storage: Storage):
        super().__init__(storage)
        self.type_return = {
            'N': State.CREATE_NEW_COLLECTION,
            'Q': State.EXIT,
            'L': State.LOAD_COLLECTION,
            'S': State.SEARCH
        }

    def handle(self, _):
        Utility.print_lines([
            '',
            '@title No active collections:',
            '@option Create [N]ew',
            '@option [L]oad collection',
            '@option [S]earch',
            '@option [Q]uit',
            ''])
        choice = Utility.prompt_user_for_input(options = ['N','L','S','Q'])
        return self.type_return[choice], None
        
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

class HandlerActiveCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, collection: Collection):
        ref_lines, ref_options = self.__build_references(collection.references)
        opt_lines, opt_options = self.__build_options(collection.references)
        Utility.print_lines([
            '',
            '@title {name}'.format(name = collection.name),
            '@subtitle {description}'.format(description = collection.description),
            '',
            '@title   References:',
            ref_lines,
            opt_lines])
        user_input = Utility.prompt_user_for_input(options=opt_options)
        if user_input == 'N':
            return State.CREATE_NEW_REFERENCE, collection
        elif user_input == 'C':
            return State.NO_COLLECTIONS, collection
        elif user_input == 'M':
            return State.DELETE_COLLECTION, collection
        elif user_input == 'D':
            return State.DELETE_REFERENCE, {'collection': collection, 'options': ref_options}
        else:
            return State.EDIT_REFERENCE, {'collection': collection,'options': ref_options}

    def __build_references(self, references):
        lines = []
        options = []
        if references == []:
            lines.append('@option <empty>')
        else:
            for i, reference in enumerate(references):
                lines.append('    [{index}] : {ref}'.format(index = i, ref=reference.format_console()))
                options.append(i)
        lines.append('')
        return lines, options

    def __build_options(self, references):
        lines = [
            '@option Create [N]ew reference',
            '@option [C]lose collection',
            '@option Eli[M]inate collection',
            '']
        options = ['N','C','M']
        if len(references) > 0:
            lines.insert(2,'@option [E]dit reference')
            lines.insert(3,'@option [D]elete reference')
            options.insert(2, 'E')
            options.insert(3, 'D')
        return lines, options

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

class HandlerLoadCollection(HandlerBase):
    
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        collections = self.storage.list_all_collections()
        Utility.print_lines([
            '',
            '@title List of collections:'
        ])
        if collections == []:
            Utility.print_lines([
                '@option <empty>',
                ''])
            return State.CREATE_NEW_COLLECTION, None
        else:
            def build_references():
                options = []
                lines = []
                for i, collection_name in enumerate(collections):
                    lines.append('@option [{index}] : {name}'.format(index = i, name = collection_name))
                    options.append(str(i))
                lines.append('')
                return lines, options
            lines, options = build_references()
            Utility.print_lines(lines)
            selected = Utility.prompt_user_for_input(options=options)
            collection = self.storage.find_collection_by_name(collections[int(selected)])
            return State.ACTIVE_COLLECTION, collection

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

class HandlerSearchCollection(HandlerBase):

    def __init__(self, storage: Storage):
        super().__init__(storage)
        self.handle_choice = {
            'A': State.SEARCH_BY_AUTHOR,
            'T': State.SEARCH_BY_TITLE
        }

    def handle(self, _):
        Utility.print_lines([
            '',
            '@title Search',
            '@option [A]uthor',
            '@option [T]itle',
            ''
            ])
        choice = Utility.prompt_user_for_input(options = ['A','T'])
        return self.handle_choice[choice], None

class HandlerSearchCollectionByField(HandlerBase):
    def __init__(self, storage: Storage):
        super().__init__(storage)

    @abc.abstractclassmethod
    def _reference_matches(self, reference: Reference, parameter: str) -> bool:
        pass

    @abc.abstractclassmethod
    def _prompt(self) -> str:
        pass

    def handle(self, _):
        parameter = Utility.prompt_user_for_input(text = self._prompt())
        found = []
        for collection_name in self.storage.list_all_collections():
            collection = self.storage.find_collection_by_name(collection_name)
            for reference in collection.references:
                if self._reference_matches(reference, parameter):
                    found.append((reference.format_console(),collection_name))
        Utility.print_lines([
            '',
            '@title Search result:',
            ['  [{i}] {ref} -> in collection: {col}'.format(i=i, ref=tpl[0], col=tpl[1]) for i, tpl in enumerate(found)],
            ''])
        choice = Utility.prompt_user_for_input(text = 'Open collection', options = [str(i) for i,_ in enumerate(found)])
        return State.ACTIVE_COLLECTION, self.storage.find_collection_by_name(found[int(choice)][1])
    
class HandlerSearchCollectionByAuthor(HandlerSearchCollectionByField):

    def __init__(self, storage: Storage):
        super().__init__(storage)

    def _reference_matches(self, reference: Reference, authors: str) -> bool:
        return authors in reference.authors

    def _prompt(self) -> str:
        return '(Partial) Author\'s name'

class HandlerSearchCollectionByTitle(HandlerBase):
    
    def __init__(self, storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        pass

class EditReference():

    def edit(self, reference: Reference):
        values = {}
        values['authors'] = self.prompt_user_for_input('Authors', reference.authors if reference is not None else None)
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        return values

    def prompt_user_for_input(self, label: str, current: str = None):
        if current is None:
            return Utility.prompt_user_for_input('{label}: '.format(label = label))
        else:
            value = Utility.prompt_user_for_input('{label} [{current}]: '.format(label = label, current = current))
            return value if value is not None else current

class EditBookReference(EditReference):

    def edit(self, reference: BookReference = None):
        values = super().edit(reference)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
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
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['last_access'] = self.prompt_user_for_input('Last accessed', reference.last_access if reference is not None else None)
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
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['last_access'] = self.prompt_user_for_input('Last accessed', reference.last_access if reference is not None else None)
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
            State.LOAD_COLLECTION: HandlerLoadCollection(self.storage),
            State.EDIT_REFERENCE: HandlerEditReference(self.storage),
            State.DELETE_REFERENCE: HandlerDeleteReference(self.storage),
            State.DELETE_COLLECTION: HandlerDeleteCollection(self.storage),
            State.SEARCH: HandlerSearchCollection(self.storage),
            State.SEARCH_BY_AUTHOR: HandlerSearchCollectionByAuthor(self.storage),
            State.SEARCH_BY_TITLE: HandlerSearchCollectionByTitle(self.storage)
        }

    def loop(self):
        while self.state is not State.EXIT:
            self.state, self.state_options = self.state_handlers[self.state].handle(self.state_options)



def main():
  Console().loop()