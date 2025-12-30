def unique_elements(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result
