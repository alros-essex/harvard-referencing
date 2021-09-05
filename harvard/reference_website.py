from .reference import Reference, ReferenceType

class WebsiteReference(Reference):
    """
    Class to manage Website References
    """

    def __init__(self, authors:str, year:str, title:str, url:str = None, accessed:str = None):
        super().__init__(WebsiteReference.get_type(), authors, year, title)
        self.url = url
        self.accessed = accessed

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.WEBSITE

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the article – followed by a full stop
        2. Year of publication - in (brackets)
        3. Title of the website - followed by a full stop
        4. Available from: URL
        5. Date of Access – in [square brackets] followed by a full stop

        eg: Tobak, S. (2015) 15 Business Tips Every Entrepreneur Should Know. Available from: https://www.entrepreneur.com/article/253143 [Accessed 30 July 2018].
        """
        return "{authors} ({year}) {title}. Available from: {url} [Accessed {accessed}].".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                url = self.url,
                accessed = self.accessed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, WebsiteReference):
            return False
        return super().__eq__(o) and o.url == self.url and o.accessed == self.accessed
