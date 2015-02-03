from Products.CMFCore.interfaces import IContentish
from five import grok
from plone.app.layout.viewlets.interfaces import IHtmlHead
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.twittercards.settings import ITwittercardsSettings

grok.templatedir('templates')


class TwittercardsViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(IHtmlHead)

    type_twittercard = ''

    @property
    def description(self):
        if self.type_twittercard == 'photo':
            return None
        return self.context.Description  # TODO: add correct call of description

    @property
    def image(self):
        return None  # TODO: add image

    @property
    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(ITwittercardsSettings)

    @property
    def twitter_user(self):
        return self.settings.twitter_user

    @property
    def title(self):
        return self.context.pretty_title_or_id()

    def available(self):
        settings = self.settings
        context_type = self.context.Type()
        for selected_type in settings.selected_types:
            if context_type in selected_type['allowed_types']:
                self.type_twittercard = selected_type['type_twittercard']
                return True
        return False
