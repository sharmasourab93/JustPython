"""
Python: Interview Problem
        Soroco Problem Solving Question
        Dec 2020
"""

"""
In this problem, we implement an improvement over python map generator.
The map generator takes the input of a function(f) an iterable(input)
where output is f(input).

In this problem, instead of one function, you need to map a series of
functions over an input. So, to the custom map generator, the inputs
will be a list of functions and the list of integers over which all
the functions are to be mapped one by one.

Take for example, we have functions given as
    funcs=[lambdax: x*x, lambda x: x+x], size n = 2.
    
The first function is the "square" function and second function is the
"double" function.
Let the given input be arr = [1, 2, 3, 4] size m = 4
Ouput : [2, 8, 18, 32]
calculated as y(i)+y(i) = arr(i) * arr(i).

Function Description:
Complete the function cmap below.
The function must be a generator and should return an iterable.
cmap has the following parameter(s):

    funcs[funcs[0]...funcs[n-1]]: an array of functions
    arr[arr[0]....arr[m-1]]: an array of integers
    
Constraints:
- 1 <= n <= 10
- 1 <= m <= 10^4
- funcs, is a callable function (where 0 <= i < n)

The first line contains an integer,
    n, denoting the number of elements in funcs.
Each line of the n subsequent lines (where 0<= i <= n) contains,
a string describing funcs, which is a
    lambda expression defining a function.

The next line contains an integer,
    m, denoting the number of elements in arr.
Each line i of the n subsequent lines (where 0<=i<m)
    contains an integer describing arr(i).
"""


def cmap(functions, array):
    
    for iterate in array:
        value = iterate
        for func in functions:
            value = func(value)
        yield value
        

if __name__ == '__main__':
    # Example 1
    """
    STDIN
    2
    lambda x: x * x
    lambda x: x + x
    4
    1
    2
    3
    4
    """
    """
    STDOUT
    2
    8
    18
    32
    """
    # Example 2
    """
    STDIN
    2
    lambda x: int(x/x)
    lambda x: x + x
    5
    5
    4
    3
    2
    1
    """
    """
    STDOUT
    2
    2
    2
    2
    2
    """
    n = int(input())
    funcs = list()
    
    for i in range(n):
        funcs.append(eval(input()))
        
    m = int(input())
    arr = list()
    
    for i in range(m):
        arr.append(int(input()))
    
    result = cmap(funcs, arr)
    
    for j in range(len(arr)):
        print(next(result))
