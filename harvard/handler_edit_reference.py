from harvard.handler_base import HandlerBase
from harvard.state import State
from harvard.utility import Utility
from harvard.reference import ReferenceType
from harvard.edit_reference import *

class HandlerEditReference(HandlerBase):

    def __init__(self, storage):
        super().__init__(storage)
        self.type_handler = {
            ReferenceType.BOOK: EditBookReference(),
            ReferenceType.EBOOK: EditEbookReference(),
            ReferenceType.CHAPTER_IN_EDITED_BOOK: EditChapterReference(),
            ReferenceType.VITALSOURCE: EditVitalsourceReference(),
            ReferenceType.JOURNAL_ARTICLE: EditJournalReference(),
            ReferenceType.JOURNAL_ARTICLE_ONLINE: EditJournalOnlineReference(),
            ReferenceType.WEBSITE: EditWebsiteReference(),
            ReferenceType.NEWSPAPER_ARTICLE: EditNewspaperReference(),
            ReferenceType.ELECTRONIC_NEWSPAPER_ARTICLE: EditNewspaperOnlineReference(),
            ReferenceType.RESEARCH_REPORT: EditResearchReportReference(),
            ReferenceType.RESEARCH_REPORT_ONLINE: EditResearchReportOnlineReference(),
            ReferenceType.INDIVIDUAL_CONFERENCE_PAPERS: EditConferencePapersReference(),
            ReferenceType.PERSONAL_CORRESPONDENCE: EditCorrespondenceReference(),
            ReferenceType.LECTURE_MATERIALS: EditLectureReference(),
            ReferenceType.UNITED_NATIONS_RESOLUTIONS: EditUNResolutions(),
            ReferenceType.INTERNATIONAL_TREATIES: EditTreatyResolution()
        }

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