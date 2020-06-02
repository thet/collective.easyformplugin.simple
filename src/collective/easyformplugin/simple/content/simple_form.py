from collective.easyform.interfaces import IEasyForm
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISimpleForm(IEasyForm):
    """ Marker interface and Dexterity Python Schema for SimpleForm
    """

    directives.omitted(
        "submitLabel",
        "useCancelButton",
        "resetLabel",
        "method",
        "form_tabbing",
        "default_fieldset_label",
        "unload_protection",
        "CSRFProtection",
        "forceSSL",
        # overrides
        "thanksPageOverrideAction",
        "thanksPageOverride",
        "formActionOverride",
        "onDisplayOverride",
        "afterValidationOverride",
        "headerInjection",
        "submitLabelOverride",
    )


@implementer(ISimpleForm)
class SimpleForm(Container):
    """
    """
