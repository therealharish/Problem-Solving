
def maximize_equal_numbers (n, k, a):
    freq = {}
    
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    max_freq = max(freq. values ())
    num_changes = (n - max_freq) // (k + 1) + 1
    # Return the maximum possible length of a subsequence with
    return min(max_freq + num_changes, n)


n = 3
k = 2
a = [1, 5, 6]

print(maximize_equal_numbers(n, k, a))