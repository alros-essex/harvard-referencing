from .reference import Reference, ReferenceType

class TreatyReference(Reference):
    """International Treaties, Conventions and accords"""

    def __init__(self, year:str, title:str, treaty_number:str, publication_title:str, volume:str, pages:str, url:str, accessed:str):
        """Create the reference
        
        Args:
            year: year/date of the reference
            title: title of the reference
            treaty_number: number of the treaty
            pubblication_title: title of the pubblication
            volume: volume
            pages: page numbers
            url: url
            accesse: last access on...
        Returns:
            None
        """
        super().__init__(TreatyReference.get_type(), None, year, title)
        self.treaty_number = treaty_number
        self.publication_title = publication_title
        self.volume = volume
        self.pages = pages
        self.url = url
        self.accessed = accessed

    @staticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class"""
        return ReferenceType.INTERNATIONAL_TREATIES

    def format_console(self) -> str:
        """Format the reference according to the standard
        
        1. Title of treaty – in italics
        2. Year of publication – in (brackets)
        3. Treaty no. – followed by a full stop
        4. Publication title – in italics, followed by a comma
        5. Volume – followed by a colon
        6. Page numbers – followed by a full stop
        7. Available from: URL
        8. Date of Access – in [square brackets] followed by a full stop

        eg:
        Convention relating to the status of refugees (1951) Treaty no. 2545. United Nations Treaty Series, 189: 137– 221. 
        Available from: https://treaties.un.org/doc/Publication/UNTS/Volume%20189/v189.pdf [Accessed 17 September 2015]

        Args:
            None
        Returns:
            formatted string
        """
        return '{title} ({year}) Treaty no. {treaty_number}. \x1B[3m{publication_title}\x1B[0m, {volume}: {pages}. Available from: {url} [Accessed {accessed}].'.format(
            title = self.title,
            year = self.year,
            treaty_number = self.treaty_number,
            publication_title = self.publication_title,
            volume = self.volume,
            pages = self.pages,
            url = self.url,
            accessed = self.accessed)

    def __eq__(self, o: object) -> bool:
        """check for equality
        
        Args:
            o: object
        Returns:
            bool, true if equal
        """
        if not isinstance(o, TreatyReference):
            return False
        return super().__eq__(o) and o.treaty_number == self.treaty_number and o.publication_title == self.publication_title \
        and o.volume == self.volume and o.pages == self.pages and o.url == self.url and o.accessed == self.accessed