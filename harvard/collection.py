from .reference import Reference

class Collection():

    def __init__(self, name:str, description:str, references = []):
        self.name = name
        self.description = description
        self.references = references

    def add_reference(self, reference: Reference):
        self.references.append(reference)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Collection):
            return False
        return o.name == self.name and o.description == self.description and o.references == self.references
