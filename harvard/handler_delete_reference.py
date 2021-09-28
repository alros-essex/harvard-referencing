from harvard.handler_base import HandlerBase
from harvard.state import State
from harvard.utility import Utility

class HandlerDeleteReference(HandlerBase):
    """Handler to delete a reference"""

    def __init__(self, storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)
    
    def handle(self, data):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        options = data['options']
        collection = data['collection']
        # ask select a reference
        selection = Utility.prompt_user_for_input(text='index to delete', options = list(map(str,options)))
        collection.references.pop(int(selection))
        # remove
        self.storage.save_collection(collection)
        # go back to main view
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.DELETE_REFERENCE
