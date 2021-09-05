from .reference import Reference, ReferenceType

class ConferencePapersReference(Reference):

    def __init__(self, authors:str, year:str, title:str, conference_title:str, conference_location:str, conference_date:str,
        place:str, publisher:str, pages:str = None):
        super().__init__(ConferencePapersReference.get_type(), authors, year, title)
        self.publisher = publisher
        self.place = place
        self.conference_title = conference_title
        self.conference_location = conference_location
        self.conference_date = conference_date
        self.pages = pages

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.PERSONAL_CORRESPONDENCE

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials, editor(s) surname and initials or the organisation responsible for writing the paper – followed by a full stop
        2. Year of publication – in (brackets)
        3. Title of the paper – in ‘inverted commas’ – followed by a comma
        4. Title and subtitle (if any) of the conference - in italics – followed by a full stop
        5. Location – followed by a comma
        6. Date of conference – followed by a full stop
        7. Place of publication – followed by a colon
        8. Publisher – followed by a full stop
        9. Page references for the paper (if available) – followed by a full stop
        """
        # Cook, D. (2000) 'Developing franchised business in Scotland', Small firms: adding the spark: 
        # the 23rd ISBA national small firms policy and research conference. Robert Gordon University, Aberdeen, 15–17 November. 
        # Leeds: Institute for Small Business Affairs. 127–136.
        return "{authors} ({year}) '{title}', \x1B[3m{conference_title}\x1B[0m. {conference_location}, {conference_date}. {place}: {publisher}.{pages}".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                conference_title = self.conference_title,
                conference_location = self.conference_location,
                conference_date = self.conference_date,
                place = self.place,
                publisher = self.publisher,
                pages = super().format_optional(value = self.pages, suffix = '.'))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ConferencePapersReference):
            return False
        return super().__eq__(o) and o.publisher == self.publisher and o.place == self.place and o.pages == self.pages \
            and o.conference_date == self.conference_date and o.conference_location == self.conference_location \
            and o.conference_title == self.conference_title
