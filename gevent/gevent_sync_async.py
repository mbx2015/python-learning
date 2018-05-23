import random

import gevent

import time


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
start = time.time()
synchronous()
print(time.time() - start)

print('Asynchronous:')
start2 = time.time()
asynchronous()
print('{:2}'.format(time.time() - start2))
