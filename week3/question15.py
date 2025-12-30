def is_armstrong(n):
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    power = len(digits)
    sum_ = 0
    for d in digits:
        sum_ += d ** power
    return sum_ == n
