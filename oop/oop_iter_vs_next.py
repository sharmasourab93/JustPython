"""
Python: iter Vs next in Python Class
"""


class PowTwo:
    
    """Class to implement an iterator of powers of two"""
    
    def __init__(self, max=0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
        
if __name__ == '__main__':
    numbers = PowTwo(3)
    i = iter(numbers)
    while True:
        try:
            print(next(i))
            
        except StopIteration:
            print("Stop Iteration raised.")
            break

    # A simpler way to achieve this
    # would be to use a for loop as given below:
    print("Printing the same object value using for loop")
    for i in PowTwo(3):
        print(i)

# The advantage of using iterators is that they save resources.
