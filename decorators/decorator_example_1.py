"""
Python: Decorator Patterns In Python
        A Decorator Example 1
"""


def decorate_message(fun):

    def add_welcome(site_name):
        return "Welcome to " + fun(site_name)

    return add_welcome


@decorate_message
def site(site_name):
    return site_name


"""
The decorated method site is equivalent to:
    def site(site_name):
        return site_name
        
    decorator_object = decorate_message(site)
    print(decorator_object)
"""


if __name__ == '__main__':
    print(site("Sourab's Website"))
