from collective.easyformplugin.simple.interfaces import IConsentWidget
from plone.app.z3cform.widget import SingleCheckBoxBoolWidget
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer_only
from zope.schema.interfaces import IField


@implementer_only(IConsentWidget)
class ConsentWidget(SingleCheckBoxBoolWidget):
    """ Consent widget implementation."""

    klass = u"consent-widget"
    css = u"consent"

    @property
    def items(self):
        result = super(ConsentWidget, self).items
        for record in result:
            record["rich_label"] = self.field.rich_label.output
        return result


@adapter(IField, interfaces.IFormLayer)
@implementer(interfaces.IFieldWidget)
def ConsentFieldWidget(field, request):
    """IFieldWidget factory for ConsentWidget."""
    return FieldWidget(field, ConsentWidget(request))
