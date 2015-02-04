from five import grok
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import Interface
from collective.twittercards.settings import ITwittercardsSettings

grok.templatedir('templates')


class TwittercardsContextPropertiesView(grok.View):
    grok.name("twittercards-context-properties")
    grok.context(Interface)
    grok.require("cmf.ManagePortal")


class TwittercardsAvailableView(grok.View):
    """
    Class to represent if the twittercards are available on the current type.
    """
    grok.name("twittercards-context-available")
    grok.context(Interface)
    grok.require("zope2.View")

    def available(self):
        portal_type = self.context.portal_type
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITwittercardsSettings)
        if not settings.selected_types or \
                not settings.activate_twittercards_tags:
            return False
        for selected_type in settings.selected_types:
            if portal_type in selected_type['allowed_types']:
                return True
        return False

    def render(self, **kwargs):
        return self.available()
