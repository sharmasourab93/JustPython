"""
Python: Keyword Only Arguments
        Enforce clarity with Keyword-Only Arguments
"""


# The problem is that it's easy to confuse the position
# of the two boolean arguments that control
# the exception-ignoring behaviour.
# This can easily cause bugs that are hard to track down.
def safe_division(number, divisor,
                  ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        
        else:
            raise


# Then callers can use keyword arguments to specify
# which of the ignore flags they want to flip for specific operations.
# flags they want to flip for specific operations,
# overriding default behaviour.
# The problem is, since these keyword arguments are optional
# behaviour there's nothing forcing callers of your
# functions to use keyword arguments for clarity
# Even with the below definition of safe_division_b
# you can still call it the old way with positional arguments.
# b_result_3 = safe_division_b(1, 10**500, True, False)
def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    
    try:
        return number / divisor
    
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        
        else:
            raise


# The symbol * in the argument list indicates the end of positional
# arguments and the beginning of keyword-only arguments.
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        
        else:
            raise


if __name__ == '__main__':
    result_1 = safe_division(1, 10**500, True, False)
    result_2 = safe_division(1, 0, False, True)
    print(result_1, result_2)
    
    b_result_1 = safe_division_b(1, 0, ignore_zero_division=True)
    b_result_2 = safe_division_b(1, 10**500, ignore_overflow=True)
    print(b_result_1, b_result_2)
    
    # Following Will raise error
    #c_result_1 = safe_division_c(1, 10**500, True, False)
    c_result_2 = safe_division_c(1, 0, ignore_zero_division=True) # OK
    print(c_result_2) #, c_result_1)
