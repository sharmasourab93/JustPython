# Just Python 

`Just Python` is a work in progress either to get started with  basics or revisit Python fundamentals.

This repo makes use of Python 3.X.

## Index 

1.  Introduction  
2.  Fundamentals 
3.  Python Objects 
4.  Variables & Operators  
5.  Some more Tricks 
6.  Control Flow 
7.  Functions 
8.  Object Oriented Programming 
9.  Exception Handling 
10. Collections 
11. Decorators
12. Iterators & Generators
13. Modules - os, sys
14. Threads & Process
15. Intermediate to Advanced 
16. Python GUI 
17. More Python 
18. PEP-8 


___
## 18. PEP-8 

[PEP-8](https://www.python.org/dev/peps/pep-0008/) is the style guide for formatting Python Code. 

**Whitespace**: In Python, whitespace is syntactically significant. Python programmers are especially sensitive to the effects of whitespace on code clarity. 

- Use spaces instead of tabs for indentation 
- Use four spaces for each level of syntactically significant indenting. 
- Lines should be 79 characters in length or less. 
- Continuations of long expressions onto additional lines should be indented by four extra spaces from their normal indentation level. 
- In a file, functions and classes should be separated by two blank lines. 
- In a class, methods should be separated by one blank line. 
- Don't put spaces around list indexes, function calls, or keyword argument assignments. 
- Put one and only one space before and after variable assignments. 

**Naming** 
- Functions, variables and attributes should be in _lowercase_underscore_ format. 
- Protected instance attributes should be in __leading_underscore_ format. 
- Private instance attributes should be in _\_\_double_leading__ underscore format. 
- Classes and exceptions should be in _CapitalizedWord_ format. 
- Module-level contants should be in ALL_CAPS format. 
- Instance methods in classes should use self as the name of the first parameter(which refers to the object).
- Class method should use cls as the name of the first parameter(which refers to the class)

**Expressions and Statements**
- Use inline negation instead of negation of positive expressions. 
- Don't check for empty values by checking the length (_if len(somelist)==0_). Use _if not somelist_ and assume empty values implicitly evaluate to false
- The same thing goes for non-empty values (like [1] or 'hi'). The statement _if somelist_ is implicitly __True__ for non-empty values. 
- Avoid single-line if statements, for and while loops, and except compound statements. Spread these over multiple lines for clarity. 
- Always put import statements at the top of a file. 
- Always use absolute names for modules when importing them, not names relative to the current module's own path. For example, to import the foo module from the bar package, you should do from _bar import foo_, and not just _import foo_.
- Imports should be in sections in the following order: standard library moudles, third-party modules, your own modules. Each subsection should have imports in alphabetical order. 

##### Things to remember 

* Always follow the PEP8 style guide when writing Python code. 
* Sharing a common style with larer Python community facilitates collaboration with others. 
* Using a consistent style makes it easier to modify your own code later.  