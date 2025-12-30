def char_type(c):
    vowels = 'aeiouAEIOU'
    if c.isdigit(): return "Digit"
    elif c in vowels: return "Vowel"
    elif c.isalpha(): return "Consonant"
    else: return "Special"
