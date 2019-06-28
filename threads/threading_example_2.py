"""
Python: Using threading
        Example 2
"""
import threading


class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        counter = 2

        while counter * counter < self.number:

            if self.number % counter == 0:
                print("%d is no prime number, because %d =%d *%d" % (

                self.number, self.number, counter, self.number / counter))

                return

            counter += 1
            print("%d is a prime number" % self.number)


if __name__ == '__main__':
    threads = []
    while True:
        i = int(input("number:"))
        if i < 1:
            break

    thread = PrimeNumber(i)
    threads += [thread]
    thread.start()

    for x in threads:
        x.join()
