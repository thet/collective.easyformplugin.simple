from collective.easyform.browser.fields import EditView
from collective.easyform.browser.fields import FieldEditForm


class FieldEditForm(FieldEditForm):
    @property
    def additionalSchemata(self):
        return []


class EditView(EditView):
    form = FieldEditForm
