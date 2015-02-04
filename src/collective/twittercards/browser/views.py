from five import grok
from zope.interface import Interface


class ITwittercardsContextProperties(Interface):
    pass


class TwittercardsContextPropertiesView(grok.View):
    pass


class TwittercardsAvailableView(grok.View):
    """
    Class to represent if the twittercards are available on the current type.
    """

    def available(self):
        return True
