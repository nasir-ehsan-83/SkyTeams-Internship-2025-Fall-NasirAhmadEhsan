def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    if a == b == c: return "Equilateral"
    if a == b or b == c or a == c: return "Isosceles"
    return "Scalene"
