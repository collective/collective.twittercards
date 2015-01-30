from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivetwittercardsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.twittercards
        xmlconfig.file(
            'configure.zcml',
            collective.twittercards,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.twittercards:default')

FIXTURE = CollectivetwittercardsLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="CollectivetwittercardsLayer:Integration"
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivetwittercardsLayer:Functional"
)
