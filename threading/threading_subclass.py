import threading
import logging


class FtThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

for i in range(5):
    t = FtThread()
    t.start()
