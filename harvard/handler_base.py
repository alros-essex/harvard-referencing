from abc import abstractmethod, ABCMeta

from harvard.storage import Storage

class HandlerBase(metaclass=ABCMeta):

    def __init__(self, storage: Storage):
        self.storage = storage

    @abstractmethod
    def handle(self, option):
        pass

    @abstractmethod
    def get_state(self):
        pass