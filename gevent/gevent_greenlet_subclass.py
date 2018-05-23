import gevent
from gevent import Greenlet


class FtGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


g = FtGreenlet("Hi there!", 3)
g.start()
g.join()
