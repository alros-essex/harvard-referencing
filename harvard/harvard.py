from enum import Enum

from harvard.storage import Storage

class State(Enum):
    NO_COLLECTIONS = 'No collections'

class HandlerBase():

    def __init__(self, storage: Storage):
        self.storage = storage

    def prompt_user(self, text: str, collection: str = None) -> str:
        base = collection = '' if collection is None else '{coll}@'.format(coll = collection)
        return input('harvard{base} {text} § '.format(base = base, text = text))

class HandlerNoCollection(HandlerBase):

    def __init(self,storage: Storage):
        super().__init__(storage)

    def handle(self):
        print('input was: '+super().prompt_user('test'))

class Console:

    def __init__(self):
        self.state = State.NO_COLLECTIONS
        self.storage = Storage()
        self.state_handlers = {
            State.NO_COLLECTIONS: HandlerNoCollection(self.storage)
        }

    def loop(self):
        while True:
            self.state_handlers[self.state].handle()



def main():
  Console().loop()