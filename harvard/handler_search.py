from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class HandlerSearchCollection(HandlerBase):

    def __init__(self, storage: Storage):
        super().__init__(storage)
        self.handle_choice = {
            'A': State.SEARCH_BY_AUTHOR,
            'T': State.SEARCH_BY_TITLE
        }

    def handle(self, _):
        choice = Utility.interact([
            '',
            '@title Search',
            '@option [A]uthor',
            '@option [T]itle',
            ''
            ])
        return self.handle_choice[choice], None

    def get_state(self):
        return State.SEARCH
