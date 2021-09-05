from abc import abstractmethod, ABCMeta

from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.reference import Reference
from harvard.state import State
from harvard.utility import Utility

class HandlerSearchCollectionByField(HandlerBase, metaclass=ABCMeta):
    def __init__(self, storage: Storage):
        super().__init__(storage)

    @abstractmethod
    def _reference_matches(self, reference: Reference, parameter: str) -> bool:
        pass

    @abstractmethod
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