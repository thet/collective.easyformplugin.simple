from collective.easyform.fields import Label
from collective.easyform.validators import isChecked
from collective.easyformplugin.simple import _
from collective.easyformplugin.simple.interfaces import IConsent
from collective.easyformplugin.simple.interfaces import IDivider
from plone.app.textfield.value import RichTextValue
from plone.schemaeditor.fields import FieldFactory
from plone.supermodel.exportimport import BaseHandler
from zope.interface import implementer
from zope.interface import Invalid
from zope.schema import Bool


@implementer(IConsent)
class Consent(Bool):
    """ A field for requiring consent to a data protection policy or similar. """

    rich_label = RichTextValue(u"")
    checkbox_label = u""

    def __init__(self, rich_label=u"", checkbox_label=u"", **kw):
        if not isinstance(rich_label, RichTextValue):
            rich_label = RichTextValue(rich_label)
        self.rich_label = rich_label
        self.checkbox_label = checkbox_label
        super(Consent, self).__init__(**kw)

    def validate(self, value):
        if self.required:
            res = isChecked(value)
            if res:
                raise Invalid(res)
        super(Consent, self).validate(value)


ConsentFactory = FieldFactory(
    Consent, _(u"label_consent_field", default=u"Einwilligung")
)
ConsentHandler = BaseHandler(Consent)


@implementer(IDivider)
class Divider(Label):
    """ A custom label field that uses a different widget template. Intended as an
    alternative to the use of fieldsets."""


DividerFactory = FieldFactory(Divider, _(u"label_divider_field", default=u"Trenner"))
DividerHandler = BaseHandler(Divider)
