def intersection(arr1, arr2):
    result = []
    for num in arr1:
        if num in arr2 and num not in result:
            result.append(num)
    return result
