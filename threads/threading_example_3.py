"""
Python: Using threading
        Example 3
"""
import time
from threading import Thread as t


def sleeper(i):
    print("Thread {} sleeps for 5 seconds\n".format(i))
    time.sleep(5)
    print("Thread %d woke up\n".format(i))


if __name__ == '__main__':
    for i in range(10):
        t1 = t(target=sleeper, args=(i,))
        t1.start()