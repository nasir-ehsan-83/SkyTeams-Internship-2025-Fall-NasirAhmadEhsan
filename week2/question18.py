def multiplication_table(n, upto=10):
    result = []
    for i in range(1, upto+1):
        result.append((n, i, n*i))
    return result
