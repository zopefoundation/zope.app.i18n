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
"""A simple implementation of a Message Catalog.

"""
__docformat__ = 'restructuredtext'

from zope.interface import provider, providedBy, implementer
import time

from BTrees.OOBTree import OOBTree
from persistent import Persistent
from zope.component.interfaces import IFactory
from zope.app.i18n.interfaces import ILocalMessageCatalog
from zope.app.i18n.interfaces import NotYetImplementedError

@implementer(ILocalMessageCatalog)
@provider(IFactory)
class MessageCatalog(Persistent):

    def __init__(self, language, domain="default"):
        """Initialize the message catalog"""
        self.id  = ''
        self.title = ''
        self.description = ''
        self.language = language
        self.domain = domain
        self._messages = OOBTree()

    def getMessage(self, id):
        'See `IMessageCatalog`'
        return self._messages[id][0]

    def queryMessage(self, id, default=None):
        'See `IMessageCatalog`'
        result = self._messages.get(id)
        if result is not None:
            result = result[0]
        else:
            result = default
        return result

    def getPluralMessage(self, singular, plural, n):
        'See `IMessageCatalog`'
        raise NotYetImplementedError

    def queryPluralMessage(self, singular, plural, n, dft1=None, dft2=None):
        'See `IMessageCatalog`'
        raise NotYetImplementedError

    def getIdentifier(self):
        'See `IReadMessageCatalog`'
        return (self.language, self.domain)

    def getFullMessage(self, msgid):
        'See `IWriteMessageCatalog`'
        message = self._messages[msgid]
        return {'domain'   : self.domain,
                'language' : self.language,
                'msgid'    : msgid,
                'msgstr'   : message[0],
                'mod_time' : message[1]}

    def setMessage(self, msgid, message, mod_time=None):
        'See `IWriteMessageCatalog`'
        if mod_time is None:
            mod_time = int(time.time())
        self._messages[msgid] = (message, mod_time)

    def deleteMessage(self, msgid):
        'See `IWriteMessageCatalog`'
        del self._messages[msgid]

    def getMessageIds(self):
        'See IWriteMessageCatalog'
        return list(self._messages.keys())

    def getMessages(self):
        'See `IWriteMessageCatalog`'
        messages = []
        for message in self._messages.items():
            messages.append({'domain'   : self.domain,
                             'language' : self.language,
                             'msgid'    : message[0],
                             'msgstr'   : message[1][0],
                             'mod_time' : message[1][1]})
        return messages

    @classmethod
    def getInterfaces(cls):
        'See `IFactory`'
        return tuple(providedBy(cls))
