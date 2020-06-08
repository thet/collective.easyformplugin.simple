from collective.easyformplugin.simple.interfaces import IConsentWidget
from collective.easyformplugin.simple.interfaces import IDividerWidget
from plone.app.z3cform.widget import SingleCheckBoxBoolWidget
from Products.Five.browser import BrowserView
from Products.Five.browser.metaconfigure import ViewMixinForTemplates
from z3c.form import interfaces
from z3c.form.browser import widget
from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
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
            record["checkbox_label"] = self.field.checkbox_label
        return result


@adapter(IField, interfaces.IFormLayer)
@implementer(interfaces.IFieldWidget)
def ConsentFieldWidget(field, request):
    """IFieldWidget factory for ConsentWidget."""
    return FieldWidget(field, ConsentWidget(request))


@implementer_only(IDividerWidget)
class DividerWidget(widget.HTMLFormElement, Widget):
    """ Divider widget implementation."""

    klass = u"divider-widget"
    css = u"divider"
    value = u""

    def update(self):
        super(DividerWidget, self).update()
        widget.addFieldClass(self)


@adapter(IField, interfaces.IFormLayer)
@implementer(interfaces.IFieldWidget)
def DividerFieldWidget(field, request):
    """IFieldWidget factory for DividerWidget."""
    return FieldWidget(field, DividerWidget(request))


class DividerRenderWidget(ViewMixinForTemplates, BrowserView):
    index = ViewPageTemplateFile("divider.pt")
