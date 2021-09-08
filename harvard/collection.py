from .reference import Reference

class Collection():

    def __init__(self, name:str, description:str, references = []):
        self.name = name
        self.description = description
        self.references = references

    def add_reference(self, reference: Reference):
        self.references.append(reference)
        def compare(a:Reference, b:Reference):
            af = a.format_console()
            bf = b.format_console()
            return 0 if af == bf else 1 if af > bf else -1
        self.references.sort(key = compare)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Collection):
            return False
        return o.name == self.name and o.description == self.description and o.references == self.references
