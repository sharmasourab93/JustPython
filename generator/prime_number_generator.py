"""
Python: Prime Number Generator
# TODO: Error Prone. Fix needed.
"""


def prime(limits=100):
    num = 2
    
    while num < limits:
        if num % 2 == 0:
            num = num + 1
        else:
            for i in range(num-1, 2, -1):
                if num % i == 0:
                    break
                    
            else:
                yield num
        
        num += 1
        
            
if __name__ == '__main__':
    gen_result = prime()
    print(next(gen_result))
    print(next(gen_result))
    print(next(gen_result))
    print(next(gen_result))
