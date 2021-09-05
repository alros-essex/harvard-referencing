from .reference import Reference, ReferenceType

class BookReference(Reference):

    def __init__(self, authors:str, year:str, title:str, 
        place:str, publisher:str, volume:str = None, edition:str = None):
        super().__init__(BookReference.get_type(), authors, year, title)
        self.volume = volume
        self.edition = edition
        self.place = place
        self.publisher = publisher

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.BOOK

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
        return "{authors} ({year}) \x1B[3m{title}\x1B[0m.{volume}{edition} {place}: {publisher}.".format(
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
