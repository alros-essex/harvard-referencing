from .reference import Reference, ReferenceType

class ResearchReportOnlineReference(Reference):
    """
    class to manage research reports in electronic format
    """

    def __init__(self, authors:str, year:str, title:str, url: str, accessed: str):
        super().__init__(ResearchReportOnlineReference.get_type(), authors, year, title)
        self.url = url
        self.accessed = accessed

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.RESEARCH_REPORT_ONLINE

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the article – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title of the report – in italics – followed by a full stop
        4. Available from: URL
        5. Date of Access – in [square brackets] followed by a full stop
        
        eg: Bradshaw, J. et al. (2013) A minimum income standard for Britain: what people think. Available from: http://www.jrf.org.uk/sites/files/jrf/2226-income-poverty-standards.pdf [Accessed 24 May 2018].
        """
        return "{authors} ({year}) \x1B[3m{title}\x1B[0m. Available from: {url} [Accessed {accessed}].".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                url = self.url,
                accessed = self.accessed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ResearchReportOnlineReference):
            return False
        return super().__eq__(o) and o.url == self.url and o.accessed == self.accessed
