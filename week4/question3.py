def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    return arr[-k:] + arr[:-k]
