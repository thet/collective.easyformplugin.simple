# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from .fields import IConsent
from .fields import IConsentWidget
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
