from .reference import Reference, ReferenceType

class UNResolutionReference(Reference):

    def __init__(self, year:str, title:str, resolution_number:str, url:str, accessed:str, general_assembly:bool=False, security_council:bool=False):
        super().__init__(UNResolutionReference.get_type(), None, year, title)
        self.format = format
        self.resolution_number = resolution_number
        self.url = url
        self.accessed = accessed
        self.general_assembly = general_assembly
        self.security_council = security_council

    @staticmethod
    def get_type() -> ReferenceType:
        return ReferenceType.UNITED_NATIONS_RESOLUTIONS

    def format_console(self) -> str:
        """
        1. Organisation responsible
        2. Year of publication – in (brackets)
        3. Title – in italics
        4. Resolution number. For General Assembly Resolutions, place A/RES/ before the resolution number; for
        Security Council Resolutions, place S/RES/ before the resolution number – followed by a full stop
        5. Available from: URL
        6. Date of Access – in [square brackets] followed by a full stop
        """
        # United Nations General Assembly (1994) United Nations framework convention on climate change. Resolution A/RES/48/189. 
        # Available from: http://daccess-dds-ny.un.org/doc/UNDOC/GEN/N94/036/43/PDF/N9403643.pdf?OpenElement [Accessed 15 September 2015].
        return "United Nations {organization} ({year}) \x1B[3m{title}\x1B[0m. Resolution {prefix}/RES/{number}. Available from: {url} [Accessed {accessed}].".format(
                organization = 'General Assembly' if self.general_assembly else 'Security Council' if self.security_council else 'N.D.',
                year = self.year,
                title = self.title,
                prefix = 'A' if self.general_assembly else 'S' if self.security_council else '',
                number = self.resolution_number,
                url = self.url,
                accessed = self.accessed)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, UNResolutionReference):
            return False
        return super().__eq__(o) and o.format == self.format and o.resolution_number == self.resolution_number and \
            o.url == self.url and o.accessed == self.accessed and o.general_assembly == self.general_assembly \
            and o.security_council == self.security_council