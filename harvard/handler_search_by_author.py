from harvard.handler_search_by_field import HandlerSearchCollectionByField
from harvard.reference import Reference
from harvard.storage import Storage
from harvard.state import State

class HandlerSearchCollectionByAuthor(HandlerSearchCollectionByField):

    def __init__(self, storage: Storage):
        super().__init__(storage)

    def _reference_matches(self, reference: Reference, authors: str) -> bool:
        return authors in reference.authors if reference.authors is not None else False

    def _prompt(self) -> str:
        return '(Partial) Author\'s name'

    def get_state(self):
        return State.SEARCH_BY_AUTHOR
