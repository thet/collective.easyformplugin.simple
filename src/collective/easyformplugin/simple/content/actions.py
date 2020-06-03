from collective.easyform import easyformMessageFactory as __
from collective.easyform.actions import Action
from collective.easyform.actions import ActionFactory
from collective.easyform.actions import Mailer
from collective.easyform.browser.actions import ActionAddForm
from collective.easyform.interfaces.actions import INewAction
from collective.easyform.interfaces.actions import isValidFieldName
from collective.easyform.interfaces.mailer import IMailer
from plone.autoform import directives
from plone.schemaeditor import _ as ___
from plone.supermodel.exportimport import BaseHandler
from plone.supermodel.model import Schema
from plone.z3cform import layout
from z3c.form import field
from zope.interface import implementer
from zope.interface import Interface
from collective.easyformplugin.simple import _

import zope.schema


class ISimpleNewAction(INewAction):

    title = zope.schema.TextLine(title=___(u"Title"), required=True, default="Action")

    __name__ = zope.schema.ASCIILine(
        title=___(u"Short Name"),
        description=___(u"Used for programmatic access to the field."),
    )

    directives.omitted("__name__", "description")


class SimpleActionAddForm(ActionAddForm):
    schema = ISimpleNewAction
    fields = field.Fields()  # let fields be updated by AutoExtensibleForm.updateFields
    # Otherwise directives.omitted has no effect.

    def create(self, data):
        data["__name__"] = data["title"]  # default name = title
        # TODO check for __name__ uniqueness
        return super(SimpleActionAddForm, self).create(data)


SimpleActionAddFormPage = layout.wrap_form(SimpleActionAddForm)


class ISimpleMailer(IMailer):
    directives.omitted(
        "description",
        "cc_recipients",
        "bcc_recipients",
        "replyto_field",
        "subject_field",
        "sendCSV",
        "sendXML",
        "body_pt",
        "body_type",
        "xinfo_headers",
        "additional_headers",
        "subjectOverride",
        "senderOverride",
        "recipientOverride",
        "ccOverride",
        "bccOverride",
    )


@implementer(ISimpleMailer)
class SimpleMailer(Mailer):
    __doc__ = ISimpleMailer.__doc__

    def __init__(self, **kw):
        for i, f in ISimpleMailer.namesAndDescriptions():
            setattr(self, i, kw.pop(i, f.default))
        Action.__init__(self, **kw)


SimpleMailerAction = ActionFactory(
    SimpleMailer,
    _(u"label_simple_mailer_action", default=u"Simple Mailer"),
    "collective.easyform.AddMailers",
)
SimpleMailerHandler = BaseHandler(SimpleMailer)
