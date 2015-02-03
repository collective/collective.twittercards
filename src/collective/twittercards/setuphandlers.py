import logging

from Products.CMFCore.utils import getToolByName


logger = logging.getLogger('collective.twittercards')


def remove_configlet(site):
    conf_id = 'collective.twittercards'
    controlpanel_tool = getToolByName(site, 'portal_controlpanel')
    if controlpanel_tool:
        controlpanel_tool.unregisterConfiglet(conf_id)
        logger.log(logging.INFO, "Unregistered \"%s\" controlpanel." % conf_id)


def uninstall(context):
    if context.readDataFile('twittercards_uninstall.txt') is None:
        return
    site = context.getSite()
    remove_configlet(site)
