# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from . import errors
from .__about__ import __version__
from .check import CouchDb

__all__ = ['__version__', 'CouchDb', 'errors']