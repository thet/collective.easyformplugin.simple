from collective.easyform.browser.view import EasyFormForm
from collective.easyform.browser.view import EasyFormFormWrapper
from collective.easyform.interfaces import IEasyFormForm
from collective.easyformplugin.simple.widgets import ConsentFieldWidget
from collective.easyformplugin.simple.widgets import DividerFieldWidget
from collective.easyformplugin.simple.fields import Consent
from collective.easyformplugin.simple.fields import Divider
from plone.autoform.widgets import ParameterizedWidget
from z3c.form.browser.checkbox import CheckBoxWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import implementer
from zope.schema import Choice
from zope.schema import Set


@implementer(IEasyFormForm)
class SimpleFormForm(EasyFormForm):
    def updateWidgets(self):
        for field in self.fields.values():
            if isinstance(field.field, Consent):
                field.widgetFactory["input"] = ParameterizedWidget(ConsentFieldWidget)
            elif isinstance(field.field, Divider):
                field.widgetFactory["input"] = ParameterizedWidget(DividerFieldWidget)
            elif isinstance(field.field, Choice):
                field.widgetFactory["input"] = ParameterizedWidget(RadioFieldWidget)
            elif isinstance(field.field, Set):
                field.widgetFactory["input"] = ParameterizedWidget(CheckBoxWidget)
        super(SimpleFormForm, self).updateWidgets()


class SimpleFormFormWrapper(EasyFormFormWrapper):
    form = SimpleFormForm


SimpleFormView = SimpleFormFormWrapper
