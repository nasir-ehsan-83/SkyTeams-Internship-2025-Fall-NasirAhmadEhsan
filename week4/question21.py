def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    start, max_len = 0, 1
    for i in range(n):
        # odd length
        l, r = i, i
        while l >=0 and r < n and s[l]==s[r]:
            if r-l+1 > max_len:
                start, max_len = l, r-l+1
            l -= 1
            r += 1
        # even length
        l, r = i, i+1
        while l >=0 and r < n and s[l]==s[r]:
            if r-l+1 > max_len:
                start, max_len = l, r-l+1
            l -= 1
            r += 1
    return s[start:start+max_len]
