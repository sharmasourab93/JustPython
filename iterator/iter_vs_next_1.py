"""
Python: iter Vs next Methods 1
"""


my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print("Printing Iter object: {0}".format(my_iter))
print("Printing  Iter object in loop:")

while True:
    try:
        print(next(my_iter))
        
    except StopIteration:
        print("Stop Iteration raised.")
        break

# A much more beautiful way of
# achieving the same is through for loop.
# The advantage of using iterators is that they save resources.
