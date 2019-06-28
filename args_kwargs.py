"""
Python: Using Args & Kwargs with examples
"""


def testify(arg1,  *argv):
    print("first argument " + arg1)

    # print(type(argv))
    for arg in argv:
        print("next argument through *argv: " + arg)


#Kwargs
def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


if __name__ == '__main__':
    testify("hello", "how", "are", "you")
    hello(game="GeeksforGeeks")
