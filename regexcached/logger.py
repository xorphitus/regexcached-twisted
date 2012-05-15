# -*- coding: utf-8 -*-

"""
Provide logging function with Twisted.
"""

from twisted.python import log
from functools import wraps
from datetime import datetime

def logging(function):
    """
    logging decorator
    """
    @wraps(function)
    def _logging(*args, **kw):
        starttime = datetime.now()
        result = function(*args, **kw)
        delta = datetime.now() - starttime
        _hoge.add(delta, starttime)
        if True:
            msg =  'args: "' + str(args[1:]) + '"'
            msg = msg + ', kw: "' + str(kw) + '"'
            msg = msg + ', result: "' + result + '"'
            log.msg(str(delta) + 'ms: ' + msg)
        return result
    return _logging


def err(msg, error):
    log.err(msg + ": " + str(error))


def debug(function):
    """
    logging decorator
    """
    @wraps(function)
    def _logging(*args, **kw):
        msg =  'args: "' + str(args[1:]) + '"'
        msg = msg + ', kw: "' + str(kw) + '"'
        log.msg(msg)
        result = function(*args, **kw)
        msg = 'result: "' + result + '"'
        return result
    return _logging
