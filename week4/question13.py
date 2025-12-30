def pattern_match(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    mapping = {}
    reverse_map = {}
    for p, w in zip(pattern, words):
        if p in mapping and mapping[p] != w:
            return False
        if w in reverse_map and reverse_map[w] != p:
            return False
        mapping[p] = w
        reverse_map[w] = p
    return True
