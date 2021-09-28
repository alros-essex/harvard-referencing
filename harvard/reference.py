from abc import abstractstaticmethod,ABCMeta
from harvard.reference_type import ReferenceType

class Reference(metaclass=ABCMeta):
    """Base class of all references"""

    def __init__(self, type:ReferenceType, authors:str, year:str, title:str):
        """Create a base reference
        
        Args:
            type: ReferenceType of the reference
            authors: string with the authors
            year: yeat/date of the reference
            title: title of the reference
        Returns:
            None
        """
        self.type = type
        self.authors = authors
        self.year = year
        self.title = title

    def format_console(self) -> str:
        """It prints the reference in the Harvard Style

        This method must be overridden by subclasses

        Args:
            None
        Returns:
            Formatted string
        """
        pass

    def format_optional(self, value, prefix=' ', suffix='', default=''):
        """Convenience method to print data that may not be defined

        Args:
            value: optional value, if not None it's returned between prefix and suffix
            prefix: optional prefix
            suffix: optional suffix
            default: optional default value to be used when value is None
        Returns:
            formatted value
        """
        return default if value is None else prefix + value + suffix

    def __eq__(self, o: object) -> bool:
        """Check for equality
        
        Args:
            o: an object
        Returns:
            bool, true if equals
        """
        if not isinstance(o, Reference):
            return False
        return o.type == self.type and o.authors == self.authors and o.year == self.year and o.title == self.title

    @abstractstaticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class

        It must be overriden by subclasses
        """
        pass