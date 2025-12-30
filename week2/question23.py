def fibonacci(n):
    if n <= 0: return []
    series = [0]
    if n == 1: return series
    series.append(1)
    for i in range(2,n):
        series.append(series[i-1]+series[i-2])
    return series
