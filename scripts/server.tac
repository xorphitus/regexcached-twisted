# -*- coding: utf-8 -*-

"""
Twisted 'tac' file for startup Device Profile Service application as a daemon process.
"""

from settings import setting
from devprof.dispatcher import CommandDispatcher

from twisted.application import internet, service
from twisted.internet import protocol
from twisted.python.logfile import DailyLogFile
from twisted.python.log import ILogObserver, FileLogObserver

disp = CommandDispatcher()

class DevProfProtocol(protocol.Protocol):
    """
    @see: L{twisted.protocol.Protocol}
    """

    def dataReceived(self, data):
        self.transport.write(disp.dispatch(data))


factory = protocol.ServerFactory()
factory.protocol = DevProfProtocol

application = service.Application(setting.APP_NAME)
logfile = DailyLogFile(setting.LOG_FILE_NAME, setting.LOG_PATH)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

server = internet.TCPServer(setting.PORT, factory)
server.setServiceParent(application)
