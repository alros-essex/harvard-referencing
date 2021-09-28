from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class HandlerSearchCollection(HandlerBase):

    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)
        # maps the key with the specialized research
        self.handle_choice = {
            'A': State.SEARCH_BY_AUTHOR,
            'T': State.SEARCH_BY_TITLE
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
            '@title Search',
            '@option [A]uthor',
            '@option [T]itle',
            ''
            ])
        return self.handle_choice[choice], None

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.SEARCH
