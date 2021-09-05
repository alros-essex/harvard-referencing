from .reference import Reference, ReferenceType

class ArticleElectronicNewpaperReference(Reference):

    def __init__(self, authors:str, year:str, title:str, newspaper: str, url: str, accessed:str, pages:str = None):
        super().__init__(ArticleElectronicNewpaperReference.get_type(), authors, year, title)
        self.newspaper = newspaper
        self.pages = pages
        self.url = url
        self.accessed = accessed

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.ELECTRONIC_NEWSPAPER_ARTICLE

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the article – followed by a full stop
        2. Date of publication – in (brackets)
        3. Title of the article - followed by a full stop
        4. Title of the newspaper –in italics - followed by a full stop
        5. Page numbers of article if available – followed by a full stop
        6. Available from: URL
        7. Date of Access – in [square brackets] followed by a full stop
        """
        # Davis, K. (May 23, 2018) Ready for GDPR? 5 Tips for Marketing Leaders. Forbes. Available from:
        # https://www.forbes.com/sites/forbescontentmarketing/2018/05/23/ready-for-gdpr-5-tips-for-marketing-leaders/#367991b0c2af
        # [Accessed 24 May 2018].
        return "{authors} ({year}) {title}. \x1B[3m{newspaper}\x1B[0m.{pages} Available from: {url} [Accessed {accessed}].".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                newspaper = self.newspaper,
                pages = super().format_optional(value = self.pages, suffix='.'),
                url = self.url,
                accessed = self.accessed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ArticleElectronicNewpaperReference):
            return False
        return super().__eq__(o) and o.newspaper == self.newspaper and o.pages == self.pages and o.url == self.url and o.accessed == self.accessed
