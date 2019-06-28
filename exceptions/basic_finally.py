"""
Python: Exceptions
        try, except & finally
"""
import sys
import time


if __name__ == '__main__':
    file = None

    try:
        file = open("poem.text")
        while True:
            line = file.readline()

            if len(line) == 0:
                break

        print(line, end=" ")
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)

    except IOError:
        print("Could not find file poem.txt")

    except KeyboardInterrupt:
        print("!! You cancelled the reading from the file.")

    finally:
        if file:
            file.close()
            print("(Cleaning up:Closed the file)")