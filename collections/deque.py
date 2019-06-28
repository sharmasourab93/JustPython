"""
Python: Using collections.deque
"""
import collections


if __name__ == '__main__':

    deque = collections.deque([1, 2, 3])
    deque.append(4)
    print("The dequeque after appending()", deque)

    deque.appendleft(6)
    print("The dequeque after appending at left is:", deque)
    print("The element 2 at indequex ", deque.index(2, 0, len(deque)))

    deque.pop()
    print("The dequeque after dequeleting from right is:", deque)

    deque.popleft()
    print("The dequeque after dequeleting from left is:", deque)

    deque.reverse()
    print(deque)
