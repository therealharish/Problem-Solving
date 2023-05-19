import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

# def bisectLeft(arr, target):
#     l = 0
#     r = len(arr)-1
#     best = -1
#     while l<=r:
#         mid = (l+r)//2
#         if arr[mid] <= target:
#             best = mid
#             l = mid+1
#         else:
#             r = mid-1
#     return best

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

newArr = [0] * (n+2)
arr.sort()
for i in range(n):  
    newArr[i+1] = arr[i] + newArr[i]

ans = []
for i in queries:
    # var = bisectLeft(arr, i)
    l = 0
    r = len(arr)-1
    best = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] <= i:
            best = mid
            l = mid+1
        else:
            r = mid-1
    var = best
    sum1 = newArr[var+1] 
    sum2 = newArr[n]
    
    if (var!=-1):
        sum2 -= newArr[var+1]
    
    ans.append(((var+1) * i - sum1) + (sum2 - (n-var-1) * i))

print(*ans)
