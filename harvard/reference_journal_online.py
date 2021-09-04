from .reference import Reference, ReferenceType

class ArticleOnlineReference(Reference):

    def __init__(self, authors:str, year:str, title:str, journal: str,
        volume:str, issue:str, pages:str, url:str = None, accessed:str = None, doi:str = None):
        super().__init__(ReferenceType.JOURNAL_ARTICLE_ONLINE, authors, year, title)
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.pages = pages
        self.url = url
        self.accessed = accessed
        self.doi = doi

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the journal – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title of the article – followed by a full stop
        4. Title of the journal – in italics
        5. Volume number
        6. Issue or part number – in (brackets), followed by a colon
        7. Page numbers of article – followed by a full stop
        8. Available from: URL (Include [Date of Access]) or DOI: (if available)
        """
        #  Kilpatrick, C., Saito, H., Allegranzi, B. & Pittet, D. (2018) Preventing sepsis in health care – It’s in your hands: 
        # A World Health Organization call to action. Journal of Infection Prevention 19(3): 104-106. DOI: https://doi.org/10.1177%2F1757177418769146
        return "{authors} ({year}) {title}. \x1B[3m{journal}\x1B[0m {volume}({issue}): {pages}. {available}".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                volume = self.volume,
                issue = self.issue,
                pages = self.pages,
                journal = self.journal,
                available = self.__format_available(self))


    def __format_available(self, value:str) -> str:
        return "DOI: {doi}".format(doi = self.doi) if self.doi is not None else 'Available from: {url} [Accessed {date}]'.format(url = self.url, date = self.accessed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ArticleOnlineReference):
            return False
        return super().__eq__(o) and o.volume == self.volume and o.journal == self.journal and o.issue == self.issue \
            and o.title == self.title and o.pages == self.pages and o.doi == self.doi and o.url == self.url and o.accessed == self.accessed
