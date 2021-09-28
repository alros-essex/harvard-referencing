from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class HandlerNoCollection(HandlerBase):
    """This is the initial handler, no collection is open"""

    def __init__(self,storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)
        # map keys to states
        self.type_return = {
            'N': State.CREATE_NEW_COLLECTION,
            'Q': State.EXIT,
            'L': State.LOAD_COLLECTION,
            'S': State.SEARCH
        }

    def handle(self, _):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        choice = Utility.interact([
            '',
            '@title No active collections:',
            '@option Create [N]ew',
            '@option [L]oad collection',
            '@option [S]earch',
            '@option [Q]uit',
            ''])
        # redirect the user to the handler based on his choice
        return self.type_return[choice], None

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.NO_COLLECTIONS
