from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class Console:
    """
    application interface
    """

    def __init__(self):
        self.state = State.NO_COLLECTIONS
        self.state_options = None
        self.storage = Storage()
        self.state_handlers = Console.__find_handlers(self.storage)

    @staticmethod
    def __find_handlers(storage: Storage):
        """
        use reflection to find all non-abstract classes extending HandlerBase
        """
        handlers = {}
        for clazz in Utility.find_classes(HandlerBase):
            instance = clazz(storage)
            handlers[instance.get_state()] = instance
        return handlers

    def loop(self):
        """
        main loop of the interface: it delegates the handling to the state-dependent handler
        """
        while self.state is not State.EXIT:
            self.state, self.state_options = self.state_handlers[self.state].handle(self.state_options)

def main():
    """
    entry point: call this method to start the application
    """
    Console().loop()