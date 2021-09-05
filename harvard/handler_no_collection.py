from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

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

    def get_state(self):
        return State.NO_COLLECTIONS
