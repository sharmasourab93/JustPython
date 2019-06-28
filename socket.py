"""
Python: Using socket
#TODO: Learning socket method
"""

from socket import gethostbyname, create_connection


def is_connected(hostname="graph.facebook.come"):
    try:
        host = gethostbyname(hostname)
        s = create_connection((host, 80), 2)

        return True

    except ConnectionError:
        pass

    return False


if __name__ == '__main__':
    if is_connected():
        print("Connected")

    else:
        print("No Internet")
