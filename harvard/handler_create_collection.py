import re

from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.state import State
from harvard.utility import Utility

class HandlerCreateNewCollection(HandlerBase):
    """Handler called when the user wants to create a new collection"""

    def __init__(self,storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        super().__init__(storage)

    def handle(self, _):
        """Handle the current context
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        # get some input
        Utility.print_lines([
            '',
            '@title Create new collection:',
            ''])
        name = self.__get_name()
        description = Utility.prompt_user_for_input(text = 'Input description')
        # create the collection and save it
        collection = Collection(name = name, description = description)
        self.storage.save_collection(collection)
        # next state will have this collection open
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        """Return the state handled by this handler
                
        Args:
            None
        Returns:
            state handled
        """
        return State.CREATE_NEW_COLLECTION

    def __get_name(self):
        """Ask the user to input a valid name
        
        Args:
            None
        Returns:
            the name
        """
        name = Utility.prompt_user_for_input(text = 'Input name')
        # since it will be the base of the filename...
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
        """Check if the collection's name is valid
        
        Args:
            name: proposed name
        Returns:
            bool: true, if valid
        """
        # not too short, not too long, only letters, numbers, -, and _
        return len(name)>0 \
            and len(name)<251 \
                and re.compile('^[\w\-_]([\w\-_ ]*[\w\-_])?$').match(name) is not None