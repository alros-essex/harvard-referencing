from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.edit_reference import *
from harvard.state import State
from harvard.utility import Utility
from harvard.edit_chapter import EditChapterReference
from harvard.edit_conference import EditConferencePapersReference
from harvard.edit_correspondence import EditCorrespondenceReference
from harvard.edit_journal import EditJournalReference
from harvard.edit_journal_online import EditJournalOnlineReference
from harvard.edit_lecture import EditLectureReference
from harvard.edit_newspaper import EditNewspaperReference
from harvard.edit_newspaper_online import EditNewspaperOnlineReference
from harvard.edit_reference import EditReference
from harvard.edit_reference_book import EditBookReference
from harvard.edit_reference_ebook import EditEbookReference
from harvard.edit_report import EditResearchReportReference
from harvard.edit_report_online import EditResearchReportOnlineReference
from harvard.edit_treaty import EditTreatyResolution
from harvard.edit_un_resolution import EditUNResolutionsReference
from harvard.edit_vitalsource import EditVitalsourceReference
from harvard.edit_website import EditWebsiteReference

class HandlerCreateNewReference(HandlerBase):

    def __init__(self,storage: Storage):
        super().__init__(storage)
        self.type_handler = {
            'B': EditBookReference(),
            'E': EditEbookReference(),
            'C': EditChapterReference(),
            'V': EditVitalsourceReference(),
            'J': EditJournalReference(),
            'O': EditJournalOnlineReference(),
            'W': EditWebsiteReference(),
            'N': EditNewspaperReference(),
            'S': EditNewspaperOnlineReference(),
            'R': EditResearchReportReference(),
            'A': EditResearchReportOnlineReference(),
            'I': EditConferencePapersReference(),
            'P': EditCorrespondenceReference(),
            'L': EditLectureReference(),
            'U': EditUNResolutionsReference(),
            'T': EditTreatyResolution()
        }
    
    def handle(self, collection: Collection):
        user_input = Utility.interact([
            '@title Create new reference',
            '@option [B]ook',
            '@option [E]book',
            '@option [C]hapter in edited book',
            '@option [V]vitalsource',
            '@option [J]ournal article',
            '@option J[O]urnal article online',
            '@option [W]ebsite',
            '@option [N]ewspaper article',
            '@option New[S]paer article online',
            '@option [R]esearch report',
            '@option Rese[A]rch report online',
            '@option [I]ndividual conference papers',
            '@option [P]ersonal correspondence',
            '@option [L]ecture material',
            '@option [U]N resolution',
            '@option Internationa [T]reaty'
        ])
        reference = self.type_handler[user_input].edit()
        collection.add_reference(reference)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.CREATE_NEW_REFERENCE
