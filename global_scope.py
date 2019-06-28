"""
Python : Understanding Global Scope
"""


print("Example 1")


# Example 1
def f1():
    global s
    print(s)
    s = "Me too"
    print(s)


# Example 2
a = 1


def f():
    print('Inside f(): %d'%a)


def g():
    a = 2
    print('Inside g(): %d' % a)


def h():
    global a
    print('Using Global in h(): %d' % a)
    a = 3
    print('Inside h(): %d' % a)


s = "I love GeeksForGeeks"
f1()

f()
g()
h()
print('Printing a locally/Global: %d' % a)