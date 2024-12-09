import math

def calc_math_add_01(*args):
    return sum(args)

def calc_math_multiply_01(*args):
    result = 1
    for number in args:
        result *= number
    return result

def calc_math_lcm_01(a, b):
    return abs(a * b) // math.gcd(a, b)