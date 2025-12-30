def remove_duplicates(arr):
    result = []
    seen = set()
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
