from .reference import Reference, ReferenceType

class ArticleNewpaperReference(Reference):
    """Newspaper Article"""

    def __init__(self, authors:str, year:str, title:str, newspaper: str, pages:str = None):
        """Create the reference
        
        Args:
            authors: string with all the authors
            year: year/date of the reference
            title: title of the reference
            newpaper: name of the newspaper
            pages: page numbers (optional)
        Returns:
            None
        """
        super().__init__(ArticleNewpaperReference.get_type(), authors, year, title)
        self.newspaper = newspaper
        self.pages = pages

    @staticmethod
    def get_type() -> ReferenceType:
        """It returns the ReferenceType managed by the class"""
        return ReferenceType.NEWSPAPER_ARTICLE

    def format_console(self) -> str:
        """Format the reference according to the standard
        
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the article – followed by a full stop
        2. Date of publication – in (brackets)
        3. Title of the article - followed by a full stop
        4. Title of the newspaper –in italics - followed by a full stop
        5. Page numbers of article if available – followed by a full stop
        
        eg: Wood, Z. (May 23, 2018) Marks & Spencer reports sharp drop in annual profits. The Guardian.

        Args:
            None
        Returns:
            formatted string
        """
        return "{authors} ({year}) {title}. \x1B[3m{newspaper}\x1B[0m.{pages}".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                pages = super().format_optional(value = self.pages, suffix='.'),
                newspaper = self.newspaper)

    def __eq__(self, o: object) -> bool:
        """check for equality
        
        Args:
            o: object
        Returns:
            bool, true if equal
        """
        if not isinstance(o, ArticleNewpaperReference):
            return False
        return super().__eq__(o) and o.newspaper == self.newspaper and o.pages == self.pages
