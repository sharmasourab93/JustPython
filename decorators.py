"""
Python : Decorators
"""


#Using Decorator body looks like this
"""
def decorate_message(fun):

    def addWelcome(site_name):
        return "Welcome to" + fun(site_name)

    return addWelcome

@decorate_message
def site(site_name):
    return site_name

print(site("GeeksforGeeks"))
"""


#Methods in Methods
"""
def method1():
    return 'hello world'


def method2(methodToRun):
    result=methodToRun()
    return result

print(method2(method1))
"""


#Without using Decorator body looks like this
"""
def messageWithWelcome(str):

    def addWelcome():
        return "Welcome to"
    return addWelcome()+str

def site(site_name):
    return site_name

print(messageWithWelcome(site("GeeksforGeeks")))
"""


#Real Python Example
"""
def my_decorator(func):

    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")

say_whee=my_decorator(say_whee)
say_whee()
"""


#Real Python Decorator Example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()
