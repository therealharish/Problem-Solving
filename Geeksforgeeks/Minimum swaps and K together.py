def minSwap (arr, n, k) : 
    #Complete the function
    count = 0
    for i in arr:
        if(i<=k):
            count+=1
    ws = 0
    remove = 0
    ans = float('inf')
    for we in range(len(arr)):
        curr = arr[we]
        windowLength = we-ws+1
        if(curr>k):
            remove+=1
        if(windowLength==count):
            ans = min(ans, remove)
            if(arr[ws]>k):
                remove-=1
            ws+=1
    return 0 if ans==float('inf') else ans