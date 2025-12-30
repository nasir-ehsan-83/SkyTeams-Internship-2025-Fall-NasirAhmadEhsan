def string_permutations(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i, ch in enumerate(s):
        for perm in string_permutations(s[:i]+s[i+1:]):
            perms.append(ch + perm)
    return perms
