from question24 import gcd  # reuse gcd function

def lcm(a, b):
    return (a * b) // gcd(a, b)
