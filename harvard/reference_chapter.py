from .reference import Reference, ReferenceType

class ChapterEditedBookReference(Reference):
    """
    class to manage a chapter in an edited book
    """

    def __init__(self, authors: str, year: str, title: str, 
        original_authors:str, original_title:str,
        place:str, publisher:str, pages:str, edition: str = None):
        super().__init__(ChapterEditedBookReference.get_type(), authors, year, title)
        self.original_authors = original_authors
        self.original_title = original_title
        self.edition = edition
        self.place = place
        self.publisher = publisher
        self.pages = pages

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.CHAPTER_IN_EDITED_BOOK

    def format_console(self):
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the book – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title and subtitle (if any) of chapter/section– in ‘inverted commas’ - followed by a comma
        4. The word ‘in’ – followed by a colon
        5. Author/Editor surname and initials of the book – followed by a full stop and (eds)
        6. Title and subtitle (if any) of book – in italics - followed by a full stop
        7. Place of publication – followed by a colon
        8. Publisher – followed by a full stop
        9. Page numbers of section referred to – followed by a full stop
        
        eg: Malunguza, N., Dube, S., Tchuenche, J., Hove-Musekwa, S. & Mukandavire, Z. (2009) ‘Two Strain HIV/AIDS Model and the Effects of Superinfection’, in: Tchuenche, J. & Mukandavire, Z. (eds) Advances in Disease Epidemiology. Hauppauge: Nova Science Publishers.171-195.
        """
        return '{authors} ({year}) \'{title}\', in: {original_authors} (eds) {original_title}. {place}: {publisher}.{pages}.'.format(
            authors = self.authors,
            year = super().format_optional(self.year, prefix='', default='N.D.'),
            title = self.title,
            original_authors = self.original_authors,
            original_title = self.original_title,
            place = self.place,
            publisher = self.publisher,
            pages = self.pages)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ChapterEditedBookReference):
            return False
        return super().__eq__(o) and o.orignal_authors == self.orignal_authors and o.original_title == self.original_title \
            and o.edition == self.edition and o.place == self.place and o.publisher == self.publisher and o.pages == self.pages