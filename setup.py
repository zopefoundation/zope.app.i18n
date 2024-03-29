##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.i18n package
"""

import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(name='zope.app.i18n',
      version='5.0.dev0',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='Persistent translation domains and message catalogs',
      long_description=(
          read('README.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="zope3 i18n message factory",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='http://github.com/zopefoundation/zope.app.i18n',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      python_requires='>=3.7',
      extras_require={
          'test': [
              'zope.app.component',
              'zope.testing',
              'zope.testrunner',
          ],
      },
      install_requires=[
          'BTrees >= 4.4.1',
          'persistent >= 4.2.4',
          'setuptools',
          'zope.app.publisher >= 4.0.0',
          'zope.component >= 4.3.0',
          'zope.configuration',
          'zope.container >= 4.1.0',
          'zope.i18n >= 4.2.0, != 4.5.*, != 4.6.*',
          'zope.i18nmessageid >= 4.1.0',
          'zope.interface >= 3.8.0',
          'zope.publisher >= 4.3.2',
          'zope.security',
      ],
      include_package_data=True,
      zip_safe=False,
      )
