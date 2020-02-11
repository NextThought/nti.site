#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

logger = __import__('logging').getLogger(__name__)

from zope import interface

from zope.component.zcml import utility

from zope.schema import TextLine

from nti.site.interfaces import ISiteMapping

from nti.site.site import SiteMapping


class ISiteMappingDirective(interface.Interface):
    """
    Register an :class:`ISiteMapping`
    """
    source_site_name = TextLine(title=u"The source site name")

    target_site_name = TextLine(title=u"The target site name")


def registerSiteMapping(_context, source_site_name, target_site_name):
    """
    Create and register a site mapping, as a utility under the `source_site_name`.
    """
    # Store and register in lowercase. Lookups occur with lowercased site
    # names.
    source_site_name = source_site_name.lower() if source_site_name else source_site_name
    target_site_name = target_site_name.lower() if target_site_name else target_site_name
    site_mapping = SiteMapping(source_site_name=source_site_name,
                               target_site_name=target_site_name)
    utility(_context, provides=ISiteMapping,
            component=site_mapping, name=source_site_name)
