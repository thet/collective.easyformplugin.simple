from collective.easyformplugin.simple import _
from plone.app.textfield import RichText
from plone.autoform import directives

import z3c.form.interfaces
import zope.schema.interfaces


class IConsent(zope.schema.interfaces.IBool):
    rich_label = RichText(
        title=_(u"Rich Label"), default=u"", required=False, missing_value=u""
    )


class IConsentWidget(z3c.form.interfaces.ISingleCheckBoxWidget):
    """ Consent Widget. """
