import gevent
import gevent.monkey
import simplejson as json
import urllib2

gevent.monkey.patch_socket()


def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = [gevent.spawn(fetch, i) for i in range(1, 10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
