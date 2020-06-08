# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from collective.easyform.interfaces import IEasyFormLayer
from collective.easyformplugin.simple import _
from plone.app.textfield import RichText
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

import z3c.form.interfaces
import zope.schema.interfaces


class IBrowserLayer(IEasyFormLayer):
    """Marker interface that defines a browser layer."""


class IConsent(zope.schema.interfaces.IBool):
    rich_label = RichText(
        title=_(u"Rich Label"), default=u"", required=False, missing_value=u""
    )
    checkbox_label = zope.schema.TextLine(
        title=_(u"Checkbox Label"), default=u"", required=False, missing_value=u""
    )


class IConsentWidget(z3c.form.interfaces.ISingleCheckBoxWidget):
    """ Consent Widget. """


class IDivider(zope.schema.interfaces.IField):
    """ Similar to a label, different display."""


class IDividerWidget(z3c.form.interfaces.IWidget):
    """ Divider Widget."""
