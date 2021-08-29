from enum import Enum

from harvard.storage import Storage

class State(Enum):
    NO_COLLECTIONS = 'No collections'

class HandlerBase():
    def prompt_user(self, text: str) -> str:
        return input(text)

class HandlerNoCollection(HandlerBase):
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
            Console.state_handlers[self.state].handle()



def main():
  Console().loop()