from enum import Enum

class ReferenceType(Enum):
    BOOK = 'book',
    EBOOK = 'ebook',
    # CHAPTER_IN_EDITED_BOOK = 'chapter_in_edited_book',
    VITALSOURCE = 'vitalsource'
    # JOURNAL_ARTICLE = 'journal_article',
    # JOURNAL_ARTICLE_ONLINE = 'journal_article_online',
    # WEBSITE = 'website',
    # NEWSPAPER_ARTICLE = 'newspaper_article',
    # ELECTRONIC_NEWSPAPER_ARTICLE = 'electronic_newspaper_article',
    # RESEARCH_REPORT = 'research_report',
    # RESEARCH_REPORT_ONLINE = 'research_report_online',
    # INDIVIDUAL_CONFERENCE_PAPERS = 'individual_conference_papers',
    # PERSONAL_CORRESPONDENCE = 'personal_correspondence',
    # LECTURE_MATERIALS = 'lecture_materials',
    # UNITED_NATIONS_RESOLUTIONS = 'united_nations_resolutions',
    # INTERNATIONAL_TREATIES = 'international_treaties'


class Reference():

    def __init__(self, user, collection, type, authors, year, title, journal, volume,
        edition, issue, place_of_publication, publisher, available_from_url, date_of_access,page_numbers):
        self._user = user
        self._collection = collection
        self._type = type
        self._authors = authors
        self._year = year
        self._title = title
        self._journal = journal
        self._volume = volume
        self._edition = edition
        self._issue = issue
        self._place_of_publication = place_of_publication
        self._publisher = publisher
        self._available_from_url = available_from_url
        self._date_of_access = date_of_access
        self._page_numbers = page_numbers
    
    @staticmethod
    def new_book(user, collection):
        return ReferenceBuilder(user, collection, ReferenceType.BOOK)

    @staticmethod
    def new_ebook(user, collection):
        return ReferenceBuilder(user, collection, ReferenceType.EBOOK)

    @staticmethod
    def new_vitalsource(user, collection):
        return ReferenceBuilder(user, collection, ReferenceType.VITALSOURCE)

    def __format_book_html(self):
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
        return "<span>{authors} ({year}) <i>{title}</i>.{volume}{edition} {place}: {publisher}.</span>".format(
                authors = self._authors,
                year = self.__format_optional(self._year, prefix='', default='N.D.'),
                title = self._title,
                volume = self.__format_optional(self._volume),
                edition = self.__format_optional(self._edition, suffix=' ed.'),
                place = self._place_of_publication,
                publisher = self._publisher)

    def __format_ebook_html(self):
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
        return '<span>{authors} ({year}) <i>{title}</i>.{edition} {place}: {publisher}. Available from: <a href="{url}">{url}</a> [Accessed {last_access}].</span>'.format(
                authors = self._authors,
                year = self.__format_optional(self._year, prefix='', default='N.D.'),
                title = self._title,
                edition = self.__format_optional(self._edition, suffix=' ed.'),
                place = self._place_of_publication,
                publisher = self._publisher,
                url = self._available_from_url,
                last_access = self._date_of_access)

    def __format_vitalsource_html(self):
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
        return '<span>{authors} ({year}) <i>{title}</i>.{edition} {place}: {publisher}. Available via the Vitalsource Bookshelf. [Accessed {last_access}].</span>'.format(
            authors = self._authors,
            year = self.__format_optional(self._year, prefix='', default='N.D.'),
            title = self._title,
            edition = self.__format_optional(self._edition, suffix=' ed.'),
            place = self._place_of_publication,
            publisher = self._publisher,
            last_access = self._date_of_access)


    def __format_optional(self, value, prefix=' ', suffix='', default=''):
        if value is None:
            return default
        else:
            return prefix + value + suffix

    __html_mapping = {
        ReferenceType.BOOK: __format_book_html,
        ReferenceType.EBOOK: __format_ebook_html,
        ReferenceType.VITALSOURCE: __format_vitalsource_html
    }

    def format_html(self):
        return Reference.__html_mapping[self._type](self)


    def user(selt):
        return self._user

    def collection(self):
        return self._collection
    
    def type(self):
        return self._type

    def authors(self):
        return self._authors

    def year(self):
        return self._year

    def title(self):
        return self._title

    def journal(self):
        return self._journal

    def volume(self):
        return self._volume
    
    def edition(self):
        return self._edition

    def issue(self):
        return self._issue

    def place_of_publication(self):
        return self._place_of_publication

    def publisher(self):
        return self._publisher

    def available_from_url(self):
        return self._available_from_url

    def date_of_access(self):
        return self._date_of_access

    def page_numbers(self):
        self._page_numbers

class ReferenceBuilder():
    def __init__(self, user, collection, type):
        self._user = user
        self._collection = collection
        self._type = type
        self._authors = None
        self._year = None
        self._title = None
        self._journal = None
        self._volume = None
        self._edition = None
        self._issue = None
        self._place_of_publication = None
        self._publisher = None
        self._available_from_url = None
        self._date_of_access = None
        self._page_numbers = None

    def with_authors(self, authors):
        self._authors = authors
        return self
        
    def with_year(self, year):
        self._year = year
        return self
        
    def with_title(self, title):
        self._title = title
        return self
        
    def with_journal(self, journal):
        self._journal = journal
        return self
        
    def with_volume(self, volume):
        self._volume = volume
        return self

    def with_edition(self, edition):
        self._edition = edition
        return self
        
    def with_issue(self, issue):
        self._issue = issue
        return self
        
    def with_place_of_publication(self, place_of_publication):
        self._place_of_publication = place_of_publication
        return self
        
    def with_publisher(self, publisher):
        self._publisher = publisher
        return self
    
    def with_available_from_url(self, available_from_url):
        self._available_from_url=available_from_url
        return self
        
    def with_date_of_access(self, date_of_access):
        self._date_of_access = date_of_access
        return self
        
    def with_page_numbers(self, page_numbers):
        self._page_numbers = page_numbers
        return self

    def build(self):
        return Reference(self._user, self._collection, self._type, 
            self._authors, self._year, self._title, self._journal, 
            self._volume, self._edition, self._issue, 
            self._place_of_publication, self._publisher, 
            self._available_from_url, self._date_of_access,
            self._page_numbers)