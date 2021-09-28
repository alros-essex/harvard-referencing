from abc import abstractmethod, ABCMeta

from harvard.storage import Storage

class HandlerBase(metaclass=ABCMeta):
    """Base class of Handlers"""

    def __init__(self, storage: Storage):
        """creates the instance
        
        Args:
            storage: storage singleton
        Returns:
            None
        """
        self.storage = storage

    @abstractmethod
    def handle(self, option):
        """Handle the current context
        
        to be overridden by subclasses
        
        Args:
            option: current context
        Returns:
            next state and next context
        """
        pass

    @abstractmethod
    def get_state(self):
        """Return the state handled by this handler
        
        to be overridden by subclasses
        
        Args:
            None
        Returns:
            state handled
        """
        pass