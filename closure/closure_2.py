"""
Python: Closure
        Example 2
"""


def sort_priority(values, group):
    
    def helper(x):
    
        if x in group:
            return 0, x
        
        return 1, x
    
    values.sort(key=helper)
    

def sort_priority_2(values, group):
    found = False
    
    def helper(x):
        if x in group:
            found = True
    
            return 0, x
        
        return 1, x
    
    values.sort(key=helper)
    
    return found


def sort_priority_3(values, group):
    found = False
    
    def helper(x):
        nonlocal found
        if x in group:
            found = True
        
            return 0, x
        
        return 1, x
    
    numbers.sort(key=helper)
    return found
    
    
if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    grouped = {2, 3, 5, 7}
    # found_2 = sort_priority_2(numbers, grouped)
    # found_3 = sort_priority_2(numbers, grouped)
    sort_priority(numbers, grouped)
    # print(found_2, found_3)
    print(numbers)
