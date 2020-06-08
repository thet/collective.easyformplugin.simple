# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from .fields import IConsent
from .fields import IConsentWidget
from .fields import IDivider
from .fields import IDividerWidget
from collective.easyform.interfaces import IEasyFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IEasyFormLayer):
    """Marker interface that defines a browser layer."""
