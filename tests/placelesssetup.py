##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Unit test logic for setting up and tearing down basic infrastructure


$Id: placelesssetup.py,v 1.1 2003/03/25 20:42:41 jim Exp $
"""

from zope.app.services.servicenames import Translation
from zope.component.adapter import provideAdapter
from zope.component import getServiceManager
from zope.i18n.globaltranslationservice import translationService
from zope.i18n.interfaces import IReadTranslationService as ITranslationService
from zope.i18n.interfaces import IUserPreferredCharsets
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.publisher.browser import BrowserLanguages
from zope.publisher.http import HTTPCharsets
from zope.publisher.http import IHTTPRequest

class PlacelessSetup:

    def setUp(self):
        sm = getServiceManager(None)
        defineService = sm.defineService
        provideService = sm.provideService

        defineService(Translation, ITranslationService)
        provideService(Translation, translationService)

        provideAdapter(IHTTPRequest, IUserPreferredCharsets, HTTPCharsets)
        provideAdapter(IHTTPRequest, IUserPreferredLanguages, BrowserLanguages)
