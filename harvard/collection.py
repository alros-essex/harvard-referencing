from functools import cmp_to_key
from .reference import Reference

class Collection():
    """
    Data structure representing a Collection of References
    """

    def __init__(self, name:str, description:str, references = []):
        """Create a Collection

        Args:
            name: name of the collection.
            description: a comment to describe it
            references: an optional list of References
        Returns:
            None
        """
        self.name = name
        self.description = description
        self.references = references

    def add_reference(self, reference: Reference):
        """add a reference to the collection.
        The Reference will be automatically sorted in the existing list

        Args:
            reference: the reference to add
        Returns:
            None
        """
        self.references.append(reference)
        def compare(a: Reference, b: Reference):
            # this is the comparator that sorts References alphabetically
            af = a.format_console()
            bf = b.format_console()
            return -1 if af < bf else 1 if af > bf else 0
        # sort the new reference in the list
        self.references = sorted(self.references, key = cmp_to_key(compare))

    def __eq__(self, o: object) -> bool:
        """Internal method to evaluate equivalence
        
        Args:
            o: Any
        Returns:
            bool: true if equals
        """
        if not isinstance(o, Collection):
            return False
        return o.name == self.name and o.description == self.description and o.references == self.references
