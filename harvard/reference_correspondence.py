from .reference import Reference, ReferenceType

class CorrespondenceReference(Reference):
    """Personal Correspondence"""

    def __init__(self, authors:str, year:str, title:str, date:str):
        """Create the reference
        
        Args:
            authors: string with all the authors
            year: year/date of the reference
            title: title of the reference
            date: day/month
        Returns:
            None
        """
        super().__init__(CorrespondenceReference.get_type(), authors, year, title)
        self.date = date

    @staticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class"""
        return ReferenceType.PERSONAL_CORRESPONDENCE

    def format_console(self) -> str:
        """Format the reference according to the standard
        
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the correspondence – followed by a full stop
        2. Year of communication – in (brackets)
        3. Medium of communication
        4. Receiver of communication – followed by a comma
        5. Day/month of communication – followed by a full stop
        
        eg: Walters, F. (2018) Conversation with John Stephens, 13 August.

        Args:
            None
        Returns:
            formatted string
        """
        return "{authors} ({year}) {title}, {date}.".format(
                authors = self.authors,
                year = self.year,
                title = self.title,
                date = self.date)

    def __eq__(self, o: object) -> bool:
        """check for equality
        
        Args:
            o: object
        Returns:
            bool, true if equal
        """
        if not isinstance(o, CorrespondenceReference):
            return False
        return super().__eq__(o) and o.date == self.date
