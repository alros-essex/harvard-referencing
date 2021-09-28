from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerDeleteCollection(HandlerBase):
    """Handler to delete a collection"""
    
    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def handle(self, collection:Collection):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        # we need a warning here!
        Utility.print_lines([
            '',
            '@warning Do you want to delete collection?',
            ''
            ])
        choice = Utility.prompt_user_for_input(options=['Y','N'])
        if choice == 'Y':
            self.storage.delete_collection(collection)
            # collection deleted, go back on the initial state
            return State.NO_COLLECTIONS, None
        else:
            # user changed his mind, go back to the main view
            return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.DELETE_COLLECTION
