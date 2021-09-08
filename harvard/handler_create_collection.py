import re

from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerCreateNewCollection(HandlerBase):
    def __init__(self,storage: Storage):
        super().__init__(storage)

    def handle(self, _):
        Utility.print_lines([
            '',
            '@title Create new collection:',
            ''])
        name = self.__get_name()
        description = Utility.prompt_user_for_input(text = 'Input description')
        collection = Collection(name = name, description = description)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.CREATE_NEW_COLLECTION

    def __get_name(self):
        name = Utility.prompt_user_for_input(text = 'Input name')
        while not self._is_valid_name(name):
            Utility.print_lines([
                '@warning name not allowed',
                '@subtitle please use only letters, numbers, space, -, and _',
                '@subtitle it can\'t start or end with space',
                '@subtitle max 250 characters'
            ])
            name = Utility.prompt_user_for_input(text = 'Input name')
        return name

    def _is_valid_name(self, name):
        return len(name)>0 \
            and len(name)<251 \
                and re.compile('^[\w\-_]([\w\-_ ]*[\w\-_])?$').match(name) is not None