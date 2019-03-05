# -*- coding: utf-8 -*-
"""
    armoury
    ~~~~~
    A toolbox of utility methods adding power
    to python data structures.  It follows best
    practice patterns. :copyright: © 2019 by the
    Nitin Gupta. :license: MIT, see LICENSE for
    more details.
"""

__version__ = '0.1.dev3'

from .list import powerlist
from .dict import powerdict


try:
    import builtins

    builtins.list = powerlist
    builtins.dict = powerdict
except:
    import __builtin__

    __builtin__.list = powerlist
    __builtin__.dict = powerdict
