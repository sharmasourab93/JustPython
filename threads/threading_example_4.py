"""
Python: Using threading
        Example 4
"""


import time
from threading import Thread as t


def sleeper(i):
    print("Thread {} sleeps for 5 second".format(i))
    time.sleep(5)
    print("Thread {} woke up".format(i))


if __name__ == '__main__':
    for i in range(20):
        t1 = t(target=sleeper, args=(i,))

        t1.start()
        print(t1.name)

        t1.join()
        print(t1.name)