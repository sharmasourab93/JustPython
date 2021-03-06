"""
Python: Exceptions
        try & except
"""


if __name__ == '__main__':
    file = 'Sobby.txt'

    try:
        # If the file does not exist
        # then it would throw an IOError
        fopen = open(file, 'rU')
        text = fopen.read()
        fopen.close()
    #control jumps directly to here if
    #any of the above lines throw IOError
    except FileNotFoundError:
        print("FileNotFoundError")
        try:
            raise ValueError
        except ValueError:
            print("Value Error")
    except IOError:
        print('Problem reading:' + file)
    
    print("All exceptions handled")