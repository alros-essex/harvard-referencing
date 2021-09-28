from abc import abstractmethod, ABCMeta

from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.reference import Reference
from harvard.state import State
from harvard.utility import Utility

class HandlerSearchCollectionByField(HandlerBase, metaclass=ABCMeta):
    """Handler for the research function"""

    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    @abstractmethod
    def _reference_matches(self, reference: Reference, parameter: str) -> bool:
        """Template method: subclasses must override it to return if the reference is a match for the parameter
        
        Args:
            reference: reference to test
            parameters: search param
        Returns:
            bool, true if it's a match
        """
        pass

    @abstractmethod
    def _prompt(self) -> str:
        """Message for the user, to be overridden
        
        Args:
            None
        Returns:
            message
        """
        pass

    def handle(self, _):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        parameter = Utility.prompt_user_for_input(text = self._prompt())
        found = self.__search(parameter)
        return self.__no_results() if len(found) == 0 else self.__print_results(found)

    def __search(self, parameter):
        found = []
        for collection_name in self.storage.list_all_collections():
            collection = self.storage.find_collection_by_name(collection_name)
            for reference in collection.references:
                if self._reference_matches(reference, parameter):
                    found.append((reference.format_console(),collection_name))
        return found

    def __no_results(self):
        Utility.print_lines([
                '',
                '@title Search result:',
                '@warning <no result found>',
                ''])
        return State.NO_COLLECTIONS, None

    def __print_results(self, found):
        Utility.print_lines([
            '',
            '@title Search result:',
            ['  [{i}] {ref} -> in collection: {col}'.format(i=i, ref=tpl[0], col=tpl[1]) for i, tpl in enumerate(found)],
            ''])
        choice = Utility.prompt_user_for_input(text = 'Open collection', options = [str(i) for i,_ in enumerate(found)])
        return State.ACTIVE_COLLECTION, self.storage.find_collection_by_name(found[int(choice)][1])