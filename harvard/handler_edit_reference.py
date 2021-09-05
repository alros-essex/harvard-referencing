from harvard.handler_base import HandlerBase
from harvard.state import State
from harvard.utility import Utility
from harvard.reference import ReferenceType
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
from harvard.edit_un_resolution  import EditUNResolutions
from harvard.edit_vitalsource   import EditVitalsourceReference
from harvard.edit_website  import EditWebsiteReference

class HandlerEditReference(HandlerBase):

    def __init__(self, storage):
        super().__init__(storage)
        
        self.type_handler = HandlerEditReference.__find_editors()

    @staticmethod
    def __find_editors():
        type_handlers = {}
        for editor in Utility.find_classes(EditReference):
            instance = editor()
            type_handlers[instance.get_type()] = instance
        return type_handlers

    def handle(self, data):
        options = data['options']
        collection = data['collection']
        selection = Utility.prompt_user_for_input(text = 'select the index of the reference', options = list(map(str,options)))
        reference = collection.references[int(selection)]
        Utility.print_lines([
            '',
            '@title Editing',
            ' {ref}'.format(ref = reference.format_console()),
            ''
        ])
        reference = self.type_handler[reference.type].edit(reference)
        collection.references[int(selection)] = reference
        return State.ACTIVE_COLLECTION, collection

    def get_state(self):
        return State.EDIT_REFERENCE
