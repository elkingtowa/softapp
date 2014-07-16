#!/usr/bin/env python

from pyftpdlib.log import logger
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from pyftpdlib import _depwarn, __ver__

__all__ = ['proto_cmds', 'Error', 'log', 'logline', 'logerror',
           'DummyAuthorizer', 'AuthorizerError', 'FTPHandler', 'FTPServer',
           'PassiveDTP', 'ActiveDTP', 'DTPHandler', 'ThrottledDTPHandler',
           'FileProducer', 'BufferedIteratorProducer', 'AbstractedFS']

_depwarn("pyftpdlib.ftpserver module is deprecated")


class CallLater(object):
    def __init__(self, *args, **kwargs):
        _depwarn("CallLater is deprecated; use "
                 "pyftpdlib.ioloop.IOLoop.instance().call_later() instead")
        from pyftpdlib.ioloop import IOLoop
        IOLoop.instance().call_later(*args, **kwargs)


class CallEvery(object):
    def __init__(self, *args, **kwargs):
        _depwarn("CallEvery is deprecated; use "
                 "pyftpdlib.ioloop.IOLoop.instance().call_every() instead")
        from pyftpdlib.ioloop import IOLoop
        IOLoop.instance().call_every(*args, **kwargs)


def log(msg):
    _depwarn("pyftpdlib.ftpserver.log() is deprecated")
    logger.info(msg)


def logline(msg):
    _depwarn("pyftpdlib.ftpserver.logline() is deprecated")
    logger.debug(msg)


def logerror(msg):
    _depwarn("pyftpdlib.ftpserver.logline() is deprecated")
    logger.error(msg)

"""
if __name__ == '__main__':
    from pyftpdlib import main
    main()
"""
