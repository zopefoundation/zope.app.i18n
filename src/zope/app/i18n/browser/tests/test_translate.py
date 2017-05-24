##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test Translation Domain 'Translate' screen.

"""
import unittest
from io import BytesIO

from zope.component.testing import PlacelessSetup
from zope.component.interfaces import IFactory
from zope.component.factory import Factory
from zope.component import provideAdapter, provideUtility

from zope.app.i18n.browser.translate import Translate
from zope.app.i18n.translationdomain import TranslationDomain
from zope.app.i18n.messagecatalog import MessageCatalog
from zope.i18n.interfaces import IUserPreferredCharsets

from zope.publisher.http import IHTTPRequest
from zope.publisher.http import HTTPCharsets
from zope.publisher.browser import BrowserRequest

class Translate(Translate):
    """Make Translate a valid Browser view. Usually done by ZCML."""

    def __init__(self, context, request):
        self.context = context
        self.request = request


class TranslateTest(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super(TranslateTest, self).setUp()

        # Setup the registries
        provideAdapter(HTTPCharsets, (IHTTPRequest,), IUserPreferredCharsets)

        provideUtility(Factory(MessageCatalog), IFactory,
                       'zope.app.MessageCatalog')

        domain = TranslationDomain()
        domain.domain = 'default'

        en_catalog = MessageCatalog('en', 'default')
        de_catalog = MessageCatalog('de', 'default')

        en_catalog.setMessage('short_greeting', 'Hello!')
        de_catalog.setMessage('short_greeting', 'Hallo!')

        en_catalog.setMessage('greeting', 'Hello $name, how are you?')
        de_catalog.setMessage('greeting', 'Hallo $name, wie geht es Dir?')

        domain['en-1'] = en_catalog
        domain['de-1'] = de_catalog

        self._view = Translate(domain, self._getRequest())


    def _getRequest(self, **kw):
        kw['HTTP_HOST'] = 'foo'
        request = BrowserRequest(BytesIO(), kw)
        request._cookies = {'edit_languages': 'en,de'}
        request._traversed_names = ['foo', 'bar']
        return request


    def testGetMessages(self):
        ids = sorted([m[0] for m in self._view.getMessages()])
        self.assertEqual(ids, ['greeting', 'short_greeting'])


    def testGetTranslation(self):
        self.assertEqual(self._view.getTranslation('short_greeting', 'en'),
                         'Hello!')


    def testGetAllLanguages(self):
        languages = sorted(self._view.getAllLanguages())
        self.assertEqual(languages, ['de', 'en'])


    def testGetEditLanguages(self):
        languages = sorted(self._view.getEditLanguages())
        self.assertEqual(languages, ['de', 'en'])


    def testAddDeleteLanguage(self):
        self._view.addLanguage('es')
        self.assert_('es' in self._view.getAllLanguages())
        self._view.deleteLanguages(['es'])
        self.assert_('es' not in self._view.getAllLanguages())


class TestSynchronize(unittest.TestCase):

    def test_synchronize_imports(self):
        # Trivial test that imports the module.  This would have triggered a
        # deprecation warning in previous versions.
        import zope.app.i18n.browser.synchronize


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main()
