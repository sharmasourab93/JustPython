"""
Python : Closure Example
"""


def outer_function(text):
	def inner_function():
		print(text)
	return inner_function


my_function = outer_function('Hey!')
my_function()
outer_function('hello')

lamda x: not x == x
foo = lamda x: not x == xfoo('asdf')
foo(float('nan'))
