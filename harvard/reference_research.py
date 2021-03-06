from .reference import Reference, ReferenceType

class ResearchReportReference(Reference):
    """Research Reports"""

    def __init__(self, authors:str, year:str, title:str, place: str, publisher: str):
        """Create the reference
        
        Args:
            authors: string with all the authors
            year: year/date of the reference
            title: title of the reference
            place: place of pubblication
            publisher: publisher
        Returns:
            None
        """
        super().__init__(ResearchReportReference.get_type(), authors, year, title)
        self.publisher = publisher
        self.place = place

    @staticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class"""
        return ReferenceType.RESEARCH_REPORT

    def format_console(self) -> str:
        """Format the reference according to the standard
        
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the article – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title of the report – in italics – followed by a full stop
        4. Place of publication – followed by colon
        5. Publisher – followed by a full stop

        eg: Dye, C. et al. (2013) Research for universal health coverage: World health report 2013. Luxembourg: World Health Organization.

        Args:
            None
        Returns:
            formatted string
        """
        return "{authors} ({year}) \x1B[3m{title}\x1B[0m. {place}: {publisher}.".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                place = self.place,
                publisher = self.publisher)

    def __eq__(self, o: object) -> bool:
        """check for equality
        
        Args:
            o: object
        Returns:
            bool, true if equal
        """
        if not isinstance(o, ResearchReportReference):
            return False
        return super().__eq__(o) and o.publisher == self.publisher and o.place == self.place
