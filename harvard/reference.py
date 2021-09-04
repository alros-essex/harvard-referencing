from enum import Enum

class ReferenceType(Enum):
    BOOK = 'book'
    EBOOK = 'ebook'
    CHAPTER_IN_EDITED_BOOK = 'chapter_in_edited_book'
    VITALSOURCE = 'vitalsource'
    JOURNAL_ARTICLE = 'journal_article'
    # JOURNAL_ARTICLE_ONLINE = 'journal_article_online'
    # WEBSITE = 'website'
    # NEWSPAPER_ARTICLE = 'newspaper_article'
    # ELECTRONIC_NEWSPAPER_ARTICLE = 'electronic_newspaper_article'
    # RESEARCH_REPORT = 'research_report'
    # RESEARCH_REPORT_ONLINE = 'research_report_online'
    # INDIVIDUAL_CONFERENCE_PAPERS = 'individual_conference_papers'
    # PERSONAL_CORRESPONDENCE = 'personal_correspondence'
    # LECTURE_MATERIALS = 'lecture_materials'
    # UNITED_NATIONS_RESOLUTIONS = 'united_nations_resolutions'
    # INTERNATIONAL_TREATIES = 'international_treaties'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Reference():

    def __init__(self, type:ReferenceType, authors:str, year:str, title:str):
        self.type = type
        self.authors = authors
        self.year = year
        self.title = title

    def format_console(self) -> str:
        pass

    def format_optional(self, value, prefix=' ', suffix='', default=''):
        return default if value is None else prefix + value + suffix

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Reference):
            return False
        return o.type == self.type and o.authors == self.authors and o.year == self.year and o.title == self.title
        