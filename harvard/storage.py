from .collection import Collection
from .reference import Reference

from typing import List
from typing import TypedDict

class Storage:

    def __init__(self):
        self.__collections={}
            
    def insert_collection(self, collection: Collection) -> None:
        self.__collections[collection.name] = { "collection": collection, "references": [] }

    def select_collection_by_name(self, name: str) -> Collection:
        entry = self.__collections[name]
        return entry["collection"]

    def insert_reference(self, collection: Collection, reference: Reference) -> None:
        entry = self.__collections[collection.name]
        entry["references"].append(reference)
            

    def select_references_by_collection(self, collection: Collection) -> List[Reference]:
        entry = self.__collections[collection.name]
        return entry["references"]
