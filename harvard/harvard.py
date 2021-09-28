from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.state import State
from harvard.utility import Utility

class Console:
    """Application interface. This implements the main loop"""

    def __init__(self):
        """Create the singleton"""
        # init internal state and singletons
        self.state = State.NO_COLLECTIONS
        self.state_options = None
        self.storage = Storage()
        self.state_handlers = Console.__find_handlers(self.storage)

    @staticmethod
    def __find_handlers(storage: Storage):
        """Use reflection to find all non-abstract classes extending HandlerBase

        Args:
            storage: storage to be used"
        returns:
            all Handlers found with reflection
        """
        handlers = {}
        for clazz in Utility.find_classes(HandlerBase):
            # create an instance
            instance = clazz(storage)
            # associate the instance to the corresponding internal state
            handlers[instance.get_state()] = instance
        return handlers

    def loop(self):
        """Main loop of the interface: it delegates the handling to the state-dependent handler"""
        while self.state is not State.EXIT:
            # it doesn't seem much, but it's all here!            #
            # the handler corresponding to the state processes the state_options
            # the processing returns next state and next options
            # loop until state is not EXIT
            self.state, self.state_options = self.state_handlers[self.state].handle(self.state_options)

def main():
    """Entry point: call this method to start the application"""
    Console().loop()