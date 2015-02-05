__title__ = 'collective.twittercards'
__version__ = '0.1.2'
__build__ = 0x000003
__author__ = 'Goldmund, Wyldebeast & Wunderliebe <info@gw20e.com>'
__copyright__ = '(c) 2015 Goldmund, Wyldebeast & Wunderliebe'
__license__ = 'GPL 2.0/LGPL 2.1'

from zope.i18nmessageid import MessageFactory

TwittercardsMessageFactory = MessageFactory('collective.twittercards')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
