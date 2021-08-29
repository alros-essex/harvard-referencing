from .reference import Reference
from typing import List

class Collection():

    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.references: List = []
    

#    def __eq__(self, o: object) -> bool:
#        return (isinstance(o, Collection)
#            and self._name == o._name
#            and self._description == o._description)