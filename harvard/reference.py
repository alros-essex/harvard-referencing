from abc import abstractstaticmethod
from harvard.reference_type import ReferenceType

class Reference:

    def __init__(self, type:ReferenceType, authors:str, year:str, title:str):
        self.type = type
        self.authors = authors
        self.year = year
        self.title = title

    def format_console(self) -> str:
        pass

    def format_optional(self, value, prefix=' ', suffix='', default=''):
        return default if value is None else prefix + value + suffix

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Reference):
            return False
        return o.type == self.type and o.authors == self.authors and o.year == self.year and o.title == self.title

    @abstractstaticmethod
    def get_type() -> ReferenceType:
        pass