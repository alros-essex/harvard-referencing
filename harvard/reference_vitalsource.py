from .reference import Reference, ReferenceType

class VitalsourceReference(Reference):
    """Vitalsource e-book"""

    def __init__(self, authors: str, year: str, title: str,
        place:str, publisher: str, last_access:str, edition: str = None):
        """Create the reference
        
        Args:
            authors: string with all the authors
            year: year/date of the reference
            title: title of the reference
            place: place of pubblication
            publisher: publisher
            last_access: last access on...
            edition: edition (optional)
        Returns:
            None
        """
        super().__init__(VitalsourceReference.get_type(), authors, year, title)
        self.edition = edition
        self.place = place
        self.publisher = publisher
        self.last_access = last_access

    @staticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class"""
        return ReferenceType.VITALSOURCE

    def format_console(self):
        """Format the reference according to the standard
        
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the book – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title and subtitle (if any) –in italics - followed by a full stop
        4. Edition (i.e. 2nd ed) – followed by a full stop
        5. Place of publication – followed by a colon
        6. Publisher – followed by a full stop
        7. Available via the Vitalsource Bookshelf – followed by a full stop
        8. Date of Access – in [square brackets] followed by a full stop
        
        eg: Tosey, P. & Gregory, J. (2001) Dictionary of Personal Development. Brisbane: Wiley Blackwell. Available via the Vitalsource Bookshelf. [Accessed 23 May 2018].

        Args:
            None
        Returns:
            formatted string
        """
        return '{authors} ({year}) \x1B[3m{title}\x1B[0m.{edition} {place}: {publisher}. Available via the Vitalsource Bookshelf. [Accessed {last_access}].'.format(
            authors = self.authors,
            year = super().format_optional(self.year, prefix='', default='N.D.'),
            title = self.title,
            edition = super().format_optional(self.edition, suffix=' ed.'),
            place = self.place,
            publisher = self.publisher,
            last_access = self.last_access)

    def __eq__(self, o: object) -> bool:
        """check for equality
        
        Args:
            o: object
        Returns:
            bool, true if equal
        """
        if not isinstance(o, VitalsourceReference):
            return False
        return super().__eq__(o) and o.edition == self.edition and o.place == self.place and o.publisher == self.publisher and o.last_access == self.last_access
