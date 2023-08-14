def findFirstOccurence(arr, target):
    l = 0
    h = len(arr)-1
    while l<h:
        print(l, h)
        mid = (l+h)//2
        if arr[mid] >= target:
            h = mid
        else:
            l =  mid + 1
    return h

arr = [1, 2, 3, 3, 3, 3, 3, 3, 3]
arr = [1, 2, 2, 2, 2, 2, 8, 8]
print(solve(arr, 2))

            