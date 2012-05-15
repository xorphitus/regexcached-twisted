# -*- coding: utf-8 -*-

"""
Provide memoization.

@author xorphitus
"""

from functools import wraps
from collections import OrderedDict

__cache = OrderedDict()

class Counter():
    def __init__(self):
        self.hitcnt = 0
        self.misscnt = 0
    def hit(self):
        self.hitcnt = self.hitcnt + 1
    def miss(self):
        self.misscnt = self.misscnt + 1

__counter = Counter()

def memoize(bnum):
    """
    A decorator for memoization.
    """
    def _memoize(function):
        @wraps(function)
        def __memoize(*args, **kw):
            key = args[1]
            val = None

            if key in __cache:
                val = __cache.pop(key)
                __cache[key] = val
                __counter.hit()
            else:
                val = function(*args, **kw)
                __cache[key] = val
                __counter.miss()

            while len(__cache) > bnum:
                __cache.popitem(last=False)

            return val
        return __memoize
    return _memoize

def clear_memo():
    """
    Clear the all memo.
    """
    __cache.clear()

def get_hits():
    return __counter.hitcnt

def get_misses():
    return __counter.misscnt

def get_curr_items():
    return len(__cache)
