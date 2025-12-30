def right_aligned_triangle(n):
    pattern = []
    for i in range(1, n+1):
        pattern.append(' '*(n-i) + '*'*i)
    return pattern
