# -*- coding: utf-8 -*-

"""
The core package of regexcached.

@author xorphitus
"""

import os
import re

from regexcached import memoization
from regexcached import logger
from settings import setting

CMD_GET = "get"
CMD_FLUSH_ALL = "flush_all"
CMD_STATS = "stats"

RESP_OK = "OK"
RESP_END = "END"
RESP_ERR = "ERROR"
RESP_CLIENT_ERR = "CLIENT_ERROR bad command line format"
RESP_VAL = "VALUE"

FIXED_FLAG_VAL = "0"

REQ_DELIMITER_PTN = re.compile("\\s+")

LINE_BREAK = "\r\n"

MAX_KEY_LEN = 250

class DataProvider():
    """
    Provides device profile data.
    """
    def __init__(self):
        pass


    @logger.logging
    @memoization.memoize(setting.BNUM)
    def get(self, key):

        val = None

        # TODO get value

        if val is None:
            val = get_empty()

        return val

class CommandDispatcher():
    """
    Parse requests and dispach to each method.
    """
    def __init__(self):
        self._provider = DataProvider()

    def dispatch(self, data):
        if data == None:
            return LINE_BREAK
        else:
            token = REQ_DELIMITER_PTN.split(data)
            if len(token) == 0:
                return RESP_ERR + LINE_BREAK
            else:
                method = token[0]
                if len(token) == 1:
                    key = ""
                else:
                    key = token[1]
                if len(key) > MAX_KEY_LEN:
                    return RESP_CLIENT_ERR + LINE_BREAK
                else:
                    ret = RESP_ERR + LINE_BREAK
                    if method == CMD_GET:
                        val = self._provider.get(key)
                        if val is None:
                            ret = RESP_END + LINE_BREAK
                        else:
                            ret = RESP_VAL + " " + key + " " + FIXED_FLAG_VAL + " " + str(len(val)) + LINE_BREAK
                            ret = ret + val + LINE_BREAK + RESP_END + LINE_BREAK
                    elif method == CMD_FLUSH_ALL:
                        self._flush_memo()
                        ret = RESP_OK + LINE_BREAK
                    elif method == CMD_STATS:
                        ret = self._stats()
                        ret = ret + RESP_END + LINE_BREAK

                    return ret

    """
    Provides "flush_memo" method behavior.
    """
    def _flush_memo(self):
        memoization.clear_memo()

    """
    Provides "stats" method behavior.
    """
    def _stats(self):
        ret = ""
        hits = memoization.get_hits()
        misses = memoization.get_misses()
        ret = ret + "STAT pid " + str(os.getpid()) + LINE_BREAK
        ret = ret + "STAT curr_items " + str(memoization.get_curr_items())  + LINE_BREAK
        ret = ret + "STAT cmd_get " + str(hits + misses) + LINE_BREAK
        ret = ret + "STAT get_hits " + str(hits) + LINE_BREAK
        ret = ret + "STAT get_misses " + str(misses) + LINE_BREAK
        return ret
