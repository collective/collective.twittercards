import logging

from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

from collective.twittercards.settings import ITwittercardsSettings


logger = logging.getLogger('collective.twittercards')

DEFAULTS = [
    {'allowed_types': 'Document', 'type_twittercard': 'summary',
     'image_field_name': u''},
    {'allowed_types': 'Folder', 'type_twittercard': 'summary',
     'image_field_name': u''},
    {'allowed_types': 'Image', 'type_twittercard': 'photo',
     'image_field_name': u''},
    {'allowed_types': 'News Item', 'type_twittercard': 'summary_large_image',
     'image_field_name': u'image'}
]


def remove_configlet(site):
    conf_id = 'collective.twittercards'
    controlpanel_tool = getToolByName(site, 'portal_controlpanel')
    if controlpanel_tool:
        controlpanel_tool.unregisterConfiglet(conf_id)
        logger.log(logging.INFO, "Unregistered \"%s\" controlpanel." % conf_id)


def setup_settings(site):
    """"""
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ITwittercardsSettings)
    if not settings.selected_types:
        settings.selected_types = DEFAULTS


def install(context):
    if context.readDataFile('twittercards_install.txt') is None:
        return
    site = context.getSite()
    setup_settings(site)


def uninstall(context):
    if context.readDataFile('twittercards_uninstall.txt') is None:
        return
    site = context.getSite()
    remove_configlet(site)
