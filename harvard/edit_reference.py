from abc import abstractmethod, ABCMeta
from harvard.reference import Reference, ReferenceType
from harvard.utility import Utility

class EditReference(metaclass=ABCMeta):
    """
    base class to edit a reference, subclasses implement the specific logic
    """

    def edit(self, reference: Reference):
        """
        edit the reference, subclasses must override it
        """
        values = {}
        values['authors'] = self.prompt_user_for_input('Authors', reference.authors if reference is not None else None)
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        return values

    def prompt_user_for_input(self, label: str, current: str = None):
        """
        convenient method to interact with the user
        """
        if current is None:
            return Utility.prompt_user_for_input('{label}: '.format(label = label))
        else:
            value = Utility.prompt_user_for_input('{label} [{current}]: '.format(label = label, current = current))
            return value if value is not None else current

    @abstractmethod
    def get_type(self) -> ReferenceType:
        """
        ReferenceType edited by the class
        """
        pass