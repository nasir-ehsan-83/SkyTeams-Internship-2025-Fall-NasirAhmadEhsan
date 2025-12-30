def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)
