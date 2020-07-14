# Your code here
import math
import random

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

power_table = {}
factorial_table = {}
division_table = {}
modulo_table = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    i = (x, y)
    v = None

    if i in power_table:
        v = power_table[i]

    else:
        power_table[i] = math.pow(x, y)
        v = power_table[i]

    if i in factorial_table:
        v = factorial_table[i]

    else:
        factorial_table[i] = math.factorial(v)
        v = factorial_table[i]
    
    if i in division_table:
        v = division_table[i]
    
    else:
        division_table[i] = v // (x + y)
        v = division_table[i]

    if i in modulo_table:
        v = modulo_table[i]
    
    else:
        modulo_table[i] = v % 982451653
        v = modulo_table[i]
    
    return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')



