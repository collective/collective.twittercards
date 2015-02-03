import unittest

from plone import api

from collective.twittercards.testing import INTEGRATION_TESTING
from plone.app.testing import logout, login, setRoles, TEST_USER_NAME, \
    TEST_USER_ID
from collective.twittercards.config import PROJECT_NAME


class ControlPanelTestCase(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        login(self.portal, TEST_USER_NAME)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        view = self.portal.restrictedTraverse("@@twittercards-settings")
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized

        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@twittercards-settings')

    def test_controlpanel_installed(self):
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertIn('collective.twittercards', actions)

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECT_NAME])
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertNotIn('twittercards', actions)
