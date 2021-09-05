from abc import abstractmethod

from harvard.storage import Storage

class HandlerBase():

    def __init__(self, storage: Storage):
        self.storage = storage

    @abstractmethod
    def handle(self, option):
        pass

    @abstractmethod
    def get_state(self):
        pass