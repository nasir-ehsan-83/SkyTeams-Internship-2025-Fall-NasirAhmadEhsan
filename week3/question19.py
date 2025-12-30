def pyramid(n):
    pattern = []
    for i in range(1, n+1):
        pattern.append(' '*(n-i) + '*'*(2*i-1))
    return pattern
