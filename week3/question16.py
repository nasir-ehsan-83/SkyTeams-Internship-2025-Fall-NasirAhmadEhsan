def fibonacci(n):
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq
