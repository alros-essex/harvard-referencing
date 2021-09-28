from harvard.handler_search_by_field import HandlerSearchCollectionByField
from harvard.storage import Storage
from harvard.state import State
from harvard.reference import Reference

class HandlerSearchCollectionByTitle(HandlerSearchCollectionByField):
    """This is a specialization of the basic find. It searches by Title"""
    
    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def _reference_matches(self, reference: Reference, title: str) -> bool:
        """Matches the reference with the criteria
        
        Args:
            reference: reference to test
            title: search string
        Returns:
            bool, true if there's a match
        """
        return title in reference.title if reference.title is not None else False

    def _prompt(self) -> str:
        """Message for the user
        
        Args:
            None
        Returns:
            message
        """
        return '(Partial) Title'

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.SEARCH_BY_TITLE


