def simple_interest(p, r, t):
    return (p * r * t) // 100

def compound_interest(p, r, t):
    amount = p
    for _ in range(t):
        amount = amount + (amount * r // 100)
    return amount - p
