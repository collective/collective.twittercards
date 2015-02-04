from Products.CMFCore.interfaces import ISiteRoot
from five import grok
from plone.app.registry.browser.controlpanel import RegistryEditForm, \
    ControlPanelFormWrapper
from plone.directives import form
from plone.z3cform import layout
from z3c.form import field
from zope.interface import Interface
from zope import schema
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow

from collective.twittercards import TwittercardsMessageFactory as _
from collective.twittercards.vocabulary import twittercards_vocabulary


class ITwittercardsTypeSettings(Interface):
    allowed_types = schema.Choice(
        title=_("label_allowed_types",
                default="Portal types"),
        description=_("Activate types for twittercards"),
        vocabulary="plone.app.vocabularies.ReallyUserFriendlyTypes",
        required=False
    )
    type_twittercard = schema.Choice(
        title=_("label_type_twittercard",
                default="Type of Twittercard"),
        description=_(""),
        vocabulary=twittercards_vocabulary,
        required=False
    )

    image_field_name = schema.TextLine(
        title=_("label_image_field_name",
                default="Image Field Name"),
        required=False
    )


class ITwittercardsSettings(form.Schema):
    activate_twittercards_tags = schema.Bool(
        title=_("label_activate_twittercards_tags",
                default="Activate Twittercards meta tags"),
        description=_("description_activate_twittercards_tags",
                      default="Controls if Twittercards are exposed to page"
                              " header."),
        default=True,
        required=False
    )

    selected_types = schema.List(
        title=_("label_selected_types",
                default="Selected twittercard types"),
        value_type=DictRow(title=_("label_selected_types_row",
                                   default="type"),
                           schema=ITwittercardsTypeSettings)
    )

    twitter_user = schema.TextLine(
        title=_("label_twitter_user", default=_("Twitter username")),
        description=_("description_twitter_user",
                      default=_("The Twitter @username the card should be "
                                "attributed to. Required for Twitter Card "
                                "analytics.")),
        required=False
    )


class TwittercardsSettingsForm(RegistryEditForm):
    schema = ITwittercardsSettings

    label = _("Twittercards configuration")
    description = _("twittercards_configlet_description",
                    default="You can select what content types are "
                            "Twittercards-enabled")
    fields = field.Fields(ITwittercardsSettings)
    fields['selected_types'].widgetFactory = DataGridFieldFactory


class TwittercardsSettingsView(grok.View):
    grok.name("twittercards-settings")
    grok.context(ISiteRoot)
    grok.require("cmf.ManagePortal")

    def render(self):
        view_factor = layout.wrap_form(TwittercardsSettingsForm,
                                       ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()
