from Products.CMFCore.interfaces import IContentish
from five import grok
from plone.app.layout.viewlets.interfaces import IHtmlHead

grok.templatedir('.')

class TestViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(IHtmlHead)
    grok.template('testviewlet.pt')
    # grok.layer(IInternetLayer)
    #
    # @property
    # def settings(self):
    #     registry = getUtility(IRegistry)
    #     return registry.forInterface(ITwittercardsSettings)
    #
    # def available(self):
    #     import pdb; pdb.set_trace()
    #     return True