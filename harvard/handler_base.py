import abc

from harvard.storage import Storage

class HandlerBase():

    def __init__(self, storage: Storage):
        self.storage = storage

    @abc.abstractmethod
    def handle(self, option):
        pass