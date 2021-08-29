from enum import Enum

class ReferenceType(Enum):
    BOOK = 'book'
    EBOOK = 'ebook'
    # CHAPTER_IN_EDITED_BOOK = 'chapter_in_edited_book'
    VITALSOURCE = 'vitalsource'
    # JOURNAL_ARTICLE = 'journal_article'
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

class BookReference(Reference):

    def __init__(self, authors:str, year:str, title:str, 
        place:str, publisher:str, volume:str = None, edition:str = None):
        super().__init__(ReferenceType.BOOK, authors, year, title)
        self.volume = volume
        self.edition = edition
        self.place = place
        self.publisher = publisher

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the book – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title and subtitle (if any) – in italics - followed by a full stop
        4. Volume number (if any) – followed by a full stop
        5. Edition (i.e. 2nd ed) – followed by a full stop
        6. Place of publication – followed by a colon
        7. Publisher – followed by a full stop
        """
        # Armstrong, G., Kotler, P. & Opresnik, O. (2016) Marketing: An Introduction. 13th ed. Harlow: Pearson Education Limited.
        return "{authors} ({year}) _{title}_.{volume}{edition} {place}: {publisher}.".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                volume = super().format_optional(self.volume),
                edition = super().format_optional(self.edition, suffix=' ed.'),
                place = self.place,
                publisher = self.publisher)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BookReference):
            return False
        return super().__eq__(o) and o.volume == self.volume and o.edition == self.edition and o.place == self.place and o.publisher == self.publisher

class EbookReference(Reference):

    def __init__(self, authors: str, year: str, title: str, 
        place: str, publisher: str, url: str, last_access:str, edition: str = None):
        super().__init__(ReferenceType.EBOOK, authors, year, title)
        self.place = place
        self.publisher = publisher
        self.url = url
        self.last_access = last_access
        self.edition = edition

    def format_console(self):
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the book – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title and subtitle (if any) –in italics - followed by a full stop
        4. Edition (i.e. 2nd ed) – followed by a full stop
        5. Place of publication – followed by a colon
        6. Publisher – followed by a full stop
        7. Available from: URL
        8. Date of Access – in [square brackets] followed by a full stop
        """
        # Raff, D. & Scranton, P. (2016) The Emergence of Routines: Entrepreneurship, Organization and Business History. 
        # Oxford: Oxford University Press. Available from: 
        # http://0- www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof- 9780198787761# 
        # [Accessed 23 May 2018].
        return '{authors} ({year}) _{title}_.{edition} {place}: {publisher}. Available from: {url} [Accessed {last_access}].'.format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                edition = super().format_optional(self.edition, suffix=' ed.'),
                place = self.place,
                publisher = self.publisher,
                url = self.url,
                last_access = self.last_access)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, EbookReference):
            return False
        return super().__eq__(o) and o.edition == self.edition and o.place == self.place and o.publisher == self.publisher and o.url == self.url and o.last_access == self.last_access

class VitalsourceReference(Reference):

    def __init__(self, authors: str, year: str, title: str,
        place:str, publisher: str, last_access:str, edition: str = None):
        super().__init__(ReferenceType.VITALSOURCE, authors, year, title)
        self.edition = edition
        self.place = place
        self.publisher = publisher
        self.last_access = last_access

    def format_console(self):
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the book – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title and subtitle (if any) –in italics - followed by a full stop
        4. Edition (i.e. 2nd ed) – followed by a full stop
        5. Place of publication – followed by a colon
        6. Publisher – followed by a full stop
        7. Available via the Vitalsource Bookshelf – followed by a full stop
        8. Date of Access – in [square brackets] followed by a full stop
        """
        # Tosey, P. & Gregory, J. (2001) Dictionary of Personal Development. Brisbane: Wiley Blackwell. Available via the Vitalsource Bookshelf. [Accessed 23 May 2018].
        return '{authors} ({year}) _{title}_.{edition} {place}: {publisher}. Available via the Vitalsource Bookshelf. [Accessed {last_access}].'.format(
            authors = self.authors,
            year = super().format_optional(self.year, prefix='', default='N.D.'),
            title = self.title,
            edition = super().format_optional(self.edition, suffix=' ed.'),
            place = self.place,
            publisher = self.publisher,
            last_access = self.last_access)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, VitalsourceReference):
            return False
        return super().__eq__(o) and o.edition == self.edition and o.place == self.place and o.publisher == self.publisher and o.last_access == self.last_access