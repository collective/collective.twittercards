from persistent import Persistent
from zope import interface
from zope import schema
from zope.annotation import factory
from zope.component import adapts
from z3c.form import field
from Products.CMFCore.interfaces import IContentish
from five import grok
from plone.directives import form

KEY = 'collective.twittercards.settings'


class ITwitterSettingsFields(interface.Interface):
    my_twitter_setting = schema.TextLine(title=u"My Twitter setting", required=False)


class TwitterSettingsFields(Persistent):
    interface.implements(ITwitterSettingsFields)
    adapts(IContentish)

TwitterSettingsFieldsFactory = factory(TwitterSettingsFields, key=KEY)


class TwitterForm(form.EditForm):
    grok.name('twitter_settings')
    grok.context(IContentish)
    grok.require('cmf.ModifyPortalContent')

    fields = field.Fields(ITwitterSettingsFields)

    def getContent(self):
        return TwitterSettingsFieldsFactory(self.context)
