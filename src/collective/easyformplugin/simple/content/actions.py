from collective.easyform import easyformMessageFactory as __
from collective.easyform.actions import Action
from collective.easyform.actions import ActionFactory
from collective.easyform.actions import Mailer
from collective.easyform.browser.actions import ActionAddForm
from collective.easyform.browser.actions import EasyFormActionsView
from collective.easyform.interfaces.actions import IEasyFormActionsContext
from collective.easyform.interfaces.actions import INewAction
from collective.easyform.interfaces.actions import isValidFieldName
from collective.easyform.interfaces.mailer import IMailer
from collective.easyformplugin.simple import _
from plone.autoform import directives
from plone.schemaeditor import _ as ___
from plone.supermodel.directives import fieldset
from plone.supermodel.exportimport import BaseHandler
from plone.supermodel.model import Schema
from plone.z3cform import layout
from z3c.form import field
from zope.interface import implementer
from zope.interface import Interface

import zope.i18nmessageid
import zope.schema


PMF = zope.i18nmessageid.MessageFactory("plone")


class ISimpleNewAction(INewAction):

    title = zope.schema.TextLine(title=___(u"Title"), required=True, default="Action")

    __name__ = zope.schema.ASCIILine(
        title=___(u"Short Name"),
        description=___(u"Used for programmatic access to the field."),
    )

    directives.omitted("__name__")


class SimpleActionAddForm(ActionAddForm):
    schema = ISimpleNewAction
    # fields = field.Fields()  # let fields be updated by AutoExtensibleForm.updateFields
    # Otherwise directives.omitted has no effect.

    def create(self, data):
        data["__name__"] = data["title"]  # default name = title
        # TODO check for __name__ uniqueness
        return super(SimpleActionAddForm, self).create(data)


SimpleActionAddFormPage = layout.wrap_form(SimpleActionAddForm)


class ISimpleMailer(IMailer):
    directives.omitted(
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

    # fieldset(
    #     u"default",
    #     label=PMF("Default"),
    #     fields=[
    #         "title",
    #         "recipient_name",
    #         "recipient_email",
    #         "to_field",
    #         "cc_recipients",
    #         "bcc_recipients",
    #         "replyto_field",
    #     ],
    #     order=1,
    # )
    # fieldset(u"addressing", label=_("Addressing"), fields=[])


@implementer(ISimpleMailer)
class SimpleMailer(Mailer):
    def __init__(self, **kw):
        # namesAndDescriptions without "all" does only iterate direct members
        # of the interface. We need to call it for ISimpleMailer and then pass
        # it over to super to let it iterate over IMailer too.
        for i, f in ISimpleMailer.namesAndDescriptions():
            setattr(self, i, kw.pop(i, f.default))
        super(SimpleMailer, self).__init__(**kw)


SimpleMailerAction = ActionFactory(
    SimpleMailer,
    _(u"label_simple_mailer_action", default=u"Simple Mailer"),
    "collective.easyform.AddMailers",
)
SimpleMailerHandler = BaseHandler(SimpleMailer)


class ISimpleFormActionsContext(IEasyFormActionsContext):
    pass


@implementer(ISimpleFormActionsContext)
class SimpleFormActionsView(EasyFormActionsView):
    pass
