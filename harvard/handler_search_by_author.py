from harvard.handler_search_by_field import HandlerSearchCollectionByField
from harvard.reference import Reference
from harvard.storage import Storage
from harvard.state import State

class HandlerSearchCollectionByAuthor(HandlerSearchCollectionByField):
    """This is a specialization of the basic find. It searches by Author"""

    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def _reference_matches(self, reference: Reference, authors: str) -> bool:
        """Matches the reference with the criteria
        
        Args:
            reference: reference to test
            authors: search string
        Returns:
            bool, true if there's a match
        """
        return authors in reference.authors if reference.authors is not None else False

    def _prompt(self) -> str:
        """Message for the user
        
        Args:
            None
        Returns:
            message
        """
        return '(Partial) Author\'s name'

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.SEARCH_BY_AUTHOR
