# Question 3: Reverse a string
def reverse_string(s):
    reversed_s = ''
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s
