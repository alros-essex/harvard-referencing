from harvard.handler_base import HandlerBase
from harvard.storage import Storage
from harvard.collection import Collection
from harvard.edit_reference import *
from harvard.state import State
from harvard.utility import Utility

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
            'U': EditUNResolutions(),
            'T': EditTreatyResolution()
        }


    def handle(self, collection: Collection):
        Utility.print_lines([
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
            '@option Rese[A]rch report online'
            '@option [I]ndividual conference papers',
            '@option [P]ersonal correspondence',
            '@option [L]ecture material',
            '@option [U]N resolution',
            '@option Internationa [T]reaty'
        ])
        user_input = Utility.prompt_user_for_input(options = ['B', 'E', 'C', 'V', 'J', 'O', 'W', 'N', 'S', 'R', 'A', 'I', 'P', 'L', 'U', 'T'])
        reference = self.type_handler[user_input].edit()
        collection.add_reference(reference)
        self.storage.save_collection(collection)
        return State.ACTIVE_COLLECTION, collection
