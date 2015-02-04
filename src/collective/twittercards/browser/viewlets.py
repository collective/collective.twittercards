from Products.CMFCore.interfaces import IContentish
from five import grok
from plone.app.layout.viewlets.interfaces import IHtmlHead
from plone.dexterity.primary import PrimaryFieldInfo
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

from collective.twittercards.settings import ITwittercardsSettings


grok.templatedir('templates')


class TwittercardsViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(IHtmlHead)
    context_settings = None

    @property
    def description(self):
        """
        If the item is a photo card, return no description.
        :return:
        """
        if self.context_settings['type_twittercard'] == 'photo':
            return None
        return getattr(self.context, 'Description', '')

    @property
    def image_field_name(self):
        card_type = self.context_settings['type_twittercard']
        if card_type in ['summary_large_image', 'summary', 'photo']:
            # Find the field that is set in the settings and return it.
            image_field = self.context_settings.get('image_field_name', '')
            if hasattr(self.context_settings, image_field):
                return image_field
        if card_type == 'photo':
            # If the image field is not set in the settings, try and find the
            # primary field.
            try:
                images = self.context.restrictedTraverse('@@images')
                if not self.is_dexterity():
                    primary = self.context.Schema().hasPrimary()
                    if images.scale(primary.getName()):
                        return primary.getName()
                else:
                    primary = PrimaryFieldInfo(self.context)
                    if images.scale(primary.fieldname):
                        return primary.fieldname
            except AttributeError:
                return None
        return None

    @property
    def has_image(self):
        portal_type = self.context.portal_type
        if portal_type == 'Image' or portal_type == 'News Item':
            return True
        return False

    @property
    def settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(ITwittercardsSettings)

    @property
    def twitter_user(self):
        return self.settings.twitter_user

    @property
    def title(self):
        """
        Return the title of an object is it is of type 'photo', otherwise use
        pretty_title_or_id() of the object.
        :return: title
        """
        if self.context_settings['type_twittercard'] == 'photo':
            return self.context.Title()
        return self.context.pretty_title_or_id()

    def is_dexterity(self):
        meta_type = self.context.meta_type
        return meta_type in ['Dexterity Item', 'Dexterity Container']

    def available(self):
        settings = self.settings
        portal_type = self.context.portal_type
        if not settings.selected_types or \
                not settings.activate_twittercards_tags:
            return False
        for selected_type in settings.selected_types:
            if portal_type in selected_type['allowed_types']:
                self.context_settings = selected_type
                if self.context_settings['type_twittercard'] == 'photo' \
                        and not self.image_field_name:
                    return False
                return True
        return False
