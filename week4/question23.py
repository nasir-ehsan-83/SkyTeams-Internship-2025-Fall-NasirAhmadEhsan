def top_k_frequent(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    freq_items = list(freq.items())
    freq_items.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in freq_items[:k]]
