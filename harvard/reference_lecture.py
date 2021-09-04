from .reference import Reference, ReferenceType

class LectureReference(Reference):

    def __init__(self, authors:str, year:str, title:str, format:str, module:str, module_title:str, organization:str):
        super().__init__(ReferenceType.LECTURE_MATERIALS, authors, year, title)
        self.format = format
        self.module = module
        self.module_title = module_title
        self.organization = organization

    def format_console(self) -> str:
        """
        1. Author(s) surname and initials responsible for writing the materials – followed by a full stop
        2. Year of publication – in (brackets)
        3. Titles of the material – in italics
        4. Format accessed through the VLE – in [square brackets] – followed by a full stop
        5. Module code – in CAPS
        6. Title of module – followed by a full stop
        7. Teaching organisation - followed by a full stop
        """
        # Smith, J. (2018) MSc BS Lecturecast 1 [Lecturecast]. MBS JUNE 2018 Business Strategy June 2018. University of Essex Online.
        return "{authors} ({year}) \x1B[3m{title}\x1B[0m [{format}]. {module} {module_title}. {organization}.".format(
                authors = self.authors,
                year = super().format_optional(self.year, prefix='', default='N.D.'),
                title = self.title,
                format = self.format,
                module = self.module.upper(),
                module_title = self.module_title,
                organization = self.organization)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, LectureReference):
            return False
        return super().__eq__(o) and o.format == self.format and o.module == self.module and o.module_title == self.module_title \
            and o.organization == self.organization
