from functools import cmp_to_key
from .reference import Reference

class Collection():

    def __init__(self, name:str, description:str, references = []):
        self.name = name
        self.description = description
        self.references = references

    def add_reference(self, reference: Reference):
        self.references.append(reference)
        sorted(self.references, key = cmp_to_key(lambda a, b: a.format_console() - b.format_console()))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Collection):
            return False
        return o.name == self.name and o.description == self.description and o.references == self.references
