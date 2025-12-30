def password_strength(password):
    if len(password) < 8:
        return 'Weak'
    has_upper = has_lower = has_digit = False
    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True
    if has_upper and has_lower and has_digit:
        return 'Strong'
    return 'Weak'
