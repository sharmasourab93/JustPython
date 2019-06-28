"""
Python: Using threading
        Example 1
"""
import threading
import time


def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    #print('worker')
    print(threading.currentThread().getName(), 'Exiting')


def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(4)
    print(threading.currentThread().getName(), 'Exiting')


if __name__ == '__main__':
    t = threading.Thread(name='my_service', target=my_service)

    w = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(target=worker)

    t.start()
    w.start()
    w2.start()