# in notes pg 99
def maxSumWithK( arr, n, k):
    forward = [0] * len(arr)
    forward[0] = arr[0]
    for i in range(1, len(arr)):
        if (forward[i - 1] + arr[i] >= arr[i]):
            forward[i] = arr[i] + forward[i - 1]
        else:
            forward[i] = arr[i]

    ws = 0
    exactK = 0
    atleastK = 0
    res = float('-inf')
    
    for i in range(k):
        exactK+=arr[i]
    res = max(res, exactK)
    
    for we in range(k, len(arr)):
        exactK += (arr[we]-arr[ws])
        atleastK = forward[ws] + exactK
        res = max(res,exactK, atleastK)
        ws+=1
    return res