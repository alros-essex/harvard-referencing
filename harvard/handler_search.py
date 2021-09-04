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
        Utility.print_lines([
            '',
            '@title Search',
            '@option [A]uthor',
            '@option [T]itle',
            ''
            ])
        choice = Utility.prompt_user_for_input(options = ['A','T'])
        return self.handle_choice[choice], None