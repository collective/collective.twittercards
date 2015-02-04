from zope.interface import Interface


class ITwittercardsContextProperties(Interface):
    pass


class TwittercardsContextPropertiesView(object):
    pass


class TwittercardsAvailableView(object):
    """
    Class to represent if the twittercards are available on the current type.
    """

    def available(self):
        return True
