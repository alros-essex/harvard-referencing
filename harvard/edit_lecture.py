from harvard.reference_lecture import LectureReference
from harvard.edit_reference import EditReference

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