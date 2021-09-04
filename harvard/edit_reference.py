from harvard.reference import Reference
from harvard.reference_book import BookReference
from harvard.reference_chapter import ChapterEditedBookReference
from harvard.reference_ebook import EbookReference
from harvard.reference_vitalsource import VitalsourceReference
from harvard.reference_journal import ArticleReference
from harvard.reference_journal_online import ArticleOnlineReference
from harvard.reference_website import WebsiteReference
from harvard.reference_newspaper import ArticleNewpaperReference
from harvard.reference_electronic_newspaper import ArticleElectronicNewpaperReference
from harvard.reference_research import ResearchReportReference
from harvard.reference_research_online import ResearchReportOnlineReference
from harvard.reference_conference import ConferencePapersReference
from harvard.reference_correspondence import CorrespondenceReference
from harvard.reference_lecture import LectureReference
from harvard.reference_un_resolution import UNResolutionReference
from harvard.reference_treaty import TreatyReference
from harvard.utility import Utility

class EditReference():

    def edit(self, reference: Reference):
        values = {}
        values['authors'] = self.prompt_user_for_input('Authors', reference.authors if reference is not None else None)
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        return values

    def prompt_user_for_input(self, label: str, current: str = None):
        if current is None:
            return Utility.prompt_user_for_input('{label}: '.format(label = label))
        else:
            value = Utility.prompt_user_for_input('{label} [{current}]: '.format(label = label, current = current))
            return value if value is not None else current

class EditBookReference(EditReference):

    def edit(self, reference: BookReference = None):
        values = super().edit(reference)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        return BookReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place = values['place'],
            publisher = values['publisher'],
            volume = values['volume'],
            edition = values['edition'])

class EditEbookReference(EditReference):

    def edit(self, reference: EbookReference = None):
        values = super().edit(reference)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['last_access'] = self.prompt_user_for_input('Last accessed', reference.last_access if reference is not None else None)
        return EbookReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place = values['place'],
            publisher = values['publisher'],
            url = values['url'],
            last_access = values['last_access'],
            edition = values['edition'])

class EditChapterReference(EditReference):

    def edit(self, reference: ChapterEditedBookReference = None):
        values = super().edit(reference)
        values['original_authors'] = self.prompt_user_for_input('Original authors', reference.original_authors if reference is not None else None)
        values['original_title'] = self.prompt_user_for_input('Original title', reference.original_title if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        return ChapterEditedBookReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            original_authors = values['original_authors'],
            original_title = values['original_title'],
            place = values['place'],
            publisher = values['publisher'],
            pages = values['pages'],
            edition = values['edition'])

class EditVitalsourceReference(EditReference):

    def edit(self, reference: VitalsourceReference = None):
        values = super().edit(reference)
        values['edition'] = self.prompt_user_for_input('Edition', reference.edition if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['last_access'] = self.prompt_user_for_input('Last accessed', reference.last_access if reference is not None else None)
        return VitalsourceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            place = values['place'],
            publisher = values['publisher'],
            last_access = values['last_access'],
            edition = values['edition'])

class EditJournalReference(EditReference):

    def edit(self, reference: ArticleReference = None):
        values = super().edit(reference)
        values['journal'] = self.prompt_user_for_input('Journal', reference.journal if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['issue'] = self.prompt_user_for_input('Issue', reference.issue if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ArticleReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            issue= values['issue'],
            journal = values['journal'],
            volume = values['volume'],
            pages = values['pages'])

class EditJournalOnlineReference(EditReference):

    def edit(self, reference: ArticleOnlineReference = None):
        values = super().edit(reference)
        values['journal'] = self.prompt_user_for_input('Journal', reference.journal if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['issue'] = self.prompt_user_for_input('Issue', reference.issue if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['doi'] = self.prompt_user_for_input('DOI', reference.doi if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ArticleOnlineReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            journal= values['journal'],
            volume= values['volume'],
            issue= values['issue'],
            pages= values['pages'],
            url= values['url'],
            accessed= values['accessed'],
            doi= values['doi'])

class EditWebsiteReference(EditReference):

    def edit(self, reference: WebsiteReference = None):
        values = super().edit(reference)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return WebsiteReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            url= values['url'],
            accessed= values['accessed'])

class EditNewspaperReference(EditReference):

    def edit(self, reference: ArticleNewpaperReference = None):
        values = super().edit(reference)
        values['newspaper'] = self.prompt_user_for_input('Newspaper', reference.newspaper if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ArticleNewpaperReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            newspaper= values['newspaper'],
            pages= values['pages'])

class EditNewspaperOnlineReference(EditReference):

    def edit(self, reference: ArticleElectronicNewpaperReference = None):
        values = super().edit(reference)
        values['newspaper'] = self.prompt_user_for_input('Newspaper', reference.newspaper if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ArticleElectronicNewpaperReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            newspaper= values['newspaper'],
            pages= values['pages'],
            url= values['url'],
            accessed= values['accessed'])

class EditResearchReportReference(EditReference):

    def edit(self, reference: ResearchReportReference = None):
        values = super().edit(reference)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        return ResearchReportReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            publisher= values['publisher'],
            place= values['place'])

class EditResearchReportOnlineReference(EditReference):

    def edit(self, reference: ResearchReportOnlineReference = None):
        values = super().edit(reference)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return ResearchReportOnlineReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            url= values['url'],
            accessed= values['accessed'])

class EditConferencePapersReference(EditReference):

    def edit(self, reference: ConferencePapersReference = None):
        values = super().edit(reference)
        values['conference_title'] = self.prompt_user_for_input('Conference title', reference.conference_title if reference is not None else None)
        values['conference_location'] = self.prompt_user_for_input('Conference location', reference.conference_location if reference is not None else None)
        values['conference_date'] = self.prompt_user_for_input('Conference date', reference.conference_date if reference is not None else None)
        values['publisher'] = self.prompt_user_for_input('Publisher', reference.publisher if reference is not None else None)
        values['place'] = self.prompt_user_for_input('Place', reference.place if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        return ConferencePapersReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            conference_title= values['conference_title'],
            conference_date= values['conference_date'],
            place= values['place'],
            publisher= values['conference_location'],
            conference_location= values['conference_location'],
            pages = values['pages'])

class EditCorrespondenceReference(EditReference):

    def edit(self, reference: CorrespondenceReference = None):
        values = {}
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Description', reference.title if reference is not None else None)
        values['date'] = self.prompt_user_for_input('Date', reference.date if reference is not None else None)
        return CorrespondenceReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            date= values['date'])

class EditLectureReference(EditReference):

    def edit(self, reference: LectureReference = None):
        values = super().edit(reference)
        values['format'] = self.prompt_user_for_input('Format', reference.format if reference is not None else None)
        values['module'] = self.prompt_user_for_input('Module code', reference.module if reference is not None else None)
        values['module_title'] = self.prompt_user_for_input('Module title', reference.module_title if reference is not None else None)
        values['organization'] = self.prompt_user_for_input('Organization', reference.organization if reference is not None else None)
        return LectureReference(
            authors = values['authors'],
            year = values['year'],
            title = values['title'],
            format= values['format'],
            module= values['module'],
            module_title= values['module_title'],
            organization= values['organization'])
                 
class EditUNResolutions(EditReference):

    def edit(self, reference: UNResolutionReference = None):
        values = {}
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        type = Utility.prompt_user_for_input(text = '[G]eneral Assembly or [S]ecurity Council', options = ['G', 'S'])
        values['resolution_number'] = self.prompt_user_for_input('Resolution number', reference.resolution_number if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return UNResolutionReference(
            year = values['year'],
            title = values['title'],
            resolution_number = values['resolution_number'],
            url = values['url'],
            accessed = values['accessed'],
            general_assembly = type == 'G',
            security_council= type == 'S')
            
class EditTreatyResolution(EditReference):

    def edit(self, reference: TreatyReference = None):
        values = {}
        values['year'] = self.prompt_user_for_input('Year', reference.year if reference is not None else None)
        values['title'] = self.prompt_user_for_input('Title', reference.title if reference is not None else None)
        values['treaty_number'] = self.prompt_user_for_input('Treaty number', reference.treaty_number if reference is not None else None)
        values['publication_title'] = self.prompt_user_for_input('Publication title', reference.publication_title if reference is not None else None)
        values['volume'] = self.prompt_user_for_input('Volume', reference.volume if reference is not None else None)
        values['pages'] = self.prompt_user_for_input('Pages', reference.pages if reference is not None else None)
        values['url'] = self.prompt_user_for_input('Url', reference.url if reference is not None else None)
        values['accessed'] = self.prompt_user_for_input('Accessed', reference.accessed if reference is not None else None)
        return TreatyReference(
            year= values['year'],
            title= values['title'],
            treaty_number= values['treaty_number'],
            publication_title= values['publication_title'],
            volume = values['volume'],
            pages = values['pages'],
            url= values['url'],
            accessed= values['accessed'])
