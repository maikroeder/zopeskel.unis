# -*- coding: utf-8 -*-
# Copyright (c) 2010 'Quadra Informatique'
# Copyright (c) 2010 'ENS Lyon - UNICES'

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
This module contains the tool of zopeskel.unices
"""
import os
from setuptools import setup, find_packages

version = '1.0'

setup(name='zopeskel.unices',
      version=version,
      description="Different kind of buildout templates used by Quadra-Informatique",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Quadra-Informatique',
      author_email='plone@quadra-informatique.fr',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopeskel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'distribute',
          # -*- Extra requirements: -*-
          'PasteScript',
          'Cheetah>1.0,<=2.2.1',
          'ZopeSkel',
          'zope.testing'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      unices_plone4_buildout = zopeskel.unices.templates:UnicesPlone4Buildout
      """,
      )