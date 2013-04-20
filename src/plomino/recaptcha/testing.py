from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class PlominorecaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plomino.recaptcha
        xmlconfig.file(
            'configure.zcml',
            plomino.recaptcha,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


PLOMINO_RECAPTCHA_FIXTURE = PlominorecaptchaLayer()
PLOMINO_RECAPTCHA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLOMINO_RECAPTCHA_FIXTURE,),
    name="PlominorecaptchaLayer:Integration"
)
PLOMINO_RECAPTCHA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLOMINO_RECAPTCHA_FIXTURE, z2.ZSERVER_FIXTURE),
    name="PlominorecaptchaLayer:Functional"
)
