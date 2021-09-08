from harvard.handler_search_by_field import HandlerSearchCollectionByField
from harvard.storage import Storage
from harvard.state import State
from harvard.reference import Reference

class HandlerSearchCollectionByTitle(HandlerSearchCollectionByField):
    
    def __init__(self, storage: Storage):
        super().__init__(storage)

    def _reference_matches(self, reference: Reference, title: str) -> bool:
        return title in reference.title if reference.title is not None else False

    def _prompt(self) -> str:
        return '(Partial) Title'

    def get_state(self):
        return State.SEARCH_BY_TITLE


