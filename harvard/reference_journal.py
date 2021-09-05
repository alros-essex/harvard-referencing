from .reference import Reference, ReferenceType

class ArticleReference(Reference):

    def __init__(self, authors:str, year:str, title:str, journal: str,
        volume:str, issue:str, pages:str):
        super().__init__(ArticleReference.get_type(), authors, year, title)
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.pages = pages

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.JOURNAL_ARTICLE

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the journal – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title of the article – followed by a full stop
        4. Title of the journal – in italics
        5. Volume number
        6. Issue or part number – in (brackets), followed by a colon
        7. Page numbers of article – followed by a full stop
        """
        # Backhaus, K., Mell, B. & Sabel, T. (2007) Business-to-Business Marketing Textbooks: A Comparative Review. Journal of Business-to-Business Marketing 14(4): 11-65.
        return "{authors} ({year}) {title}. \x1B[3m{journal}\x1B[0m {volume}({issue}): {pages}.".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                volume = self.volume,
                issue = self.issue,
                pages = self.pages,
                journal = self.journal)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ArticleReference):
            return False
        return super().__eq__(o) and o.volume == self.volume and o.journal == self.journal and o.issue == self.issue and o.pages == self.pages
