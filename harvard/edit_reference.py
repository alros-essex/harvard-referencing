from abc import abstractmethod, ABCMeta
from harvard.reference import Reference, ReferenceType
from harvard.utility import Utility

class EditReference(metaclass=ABCMeta):
    """Base class to edit a reference, subclasses implement the specific logic"""

    def edit(self, reference: Reference):
        """Edit the reference, subclasses must override it
        
        Args:
            reference: optional reference to provide default values
        Returns:
            dict with base values for authors, year, title
        """
        values = {}
        values['authors'] = self.prompt_user_for_input('Authors', reference.authors if reference is not None else None)
        values['year'] = self.prompt_user_for_input('Date', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        return values

    def prompt_user_for_input(self, label: str, current: str = None):
        """Convenient method to interact with the user

        Args:
            label: message for the user
            current: current default value
        Returns:
            str with updated value (it may be equal to current)
        """
        if current is None:
            # call Utility for proper formatting
            return Utility.prompt_user_for_input('{label}: '.format(label = label))
        else:
            # call Utility for proper formatting
            value = Utility.prompt_user_for_input('{label} [{current}]: '.format(label = label, current = current))
            return value if value is not None else current

    @abstractmethod
    def get_type(self) -> ReferenceType:
        """ReferenceType edited by the class. It must be overridden by subclasses

        Returns:
            ReferenceType handled by the editor
        """
        pass