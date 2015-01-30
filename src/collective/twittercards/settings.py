from Products.CMFCore.interfaces import ISiteRoot
from five import grok
from plone.app.controlpanel.widgets import MultiCheckBoxThreeColumnWidget
from plone.app.registry.browser.controlpanel import RegistryEditForm, \
    ControlPanelFormWrapper
from plone.directives import form
from plone.z3cform import layout
from zope.interface import Interface
from zope.schema import Bool, Tuple, Choice, TextLine, List

from collective.twittercards import TwittercardsMessageFactory as _


class ITwittercardsSettings(form.Schema):
    """TEMP"""

    activate_twittercards_tags = Bool(
        title=_("label_activate_twittercards_tags",
                default='Activate Twittercards meta tags'),
        description=_("description_activate_twittercards_tags",
                      default='Controls if Twittercards are exposed to page'
                              ' header.'),
        default=True,
        required=False
    )

    allowed_types = Tuple(
        title=_(u'Portal types'),
        description=_(u'Portal types lead image may be attached to.'),
        value_type=Choice(
            vocabulary="plone.app.vocabularies.ReallyUserFriendlyTypes"),
        required=False
    )

class TwittercardsSettingsForm(RegistryEditForm):
    schema = ITwittercardsSettings

    label = _("Twittercards configuration")
    description = _("twittercards_configlet_description",
                    default="You can select what content types are "
                            "Twittercards-enabled")


class TwittercardsSettingsView(grok.View):
    grok.name('twittercards-settings')
    grok.context(ISiteRoot)
    grok.require('cmf.ManagePortal')

    def render(self):
        view_factor = layout.wrap_form(TwittercardsSettingsForm,
                                       ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()