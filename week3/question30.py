def find_missing_number(arr, N):
    total = N*(N+1)//2
    sum_arr = 0
    for num in arr:
        sum_arr += num
    return total - sum_arr
