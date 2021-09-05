from .reference import Reference, ReferenceType

class EbookReference(Reference):
    """
    class to manage ebooks
    """

    def __init__(self, authors: str, year: str, title: str, 
        place: str, publisher: str, url: str, last_access:str, edition: str = None):
        super().__init__(EbookReference.get_type(), authors, year, title)
        self.place = place
        self.publisher = publisher
        self.url = url
        self.last_access = last_access
        self.edition = edition

    @staticmethod
    def get_type() -> ReferenceType:
        ReferenceType.EBOOK


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
        
        eg:
        Raff, D. & Scranton, P. (2016) The Emergence of Routines: Entrepreneurship, Organization and Business History. 
        Oxford: Oxford University Press. Available from: 
        http://0- www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof- 9780198787761# 
        [Accessed 23 May 2018].
        """
        return '{authors} ({year}) \x1B[3m{title}\x1B[0m.{edition} {place}: {publisher}. Available from: {url} [Accessed {last_access}].'.format(
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
