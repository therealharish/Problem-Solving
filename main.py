arr = [1,4,6,8,10]
low = 0
high = len(arr)-1
ans = 0
target = 6
while(low<=high):
    mid = (low+high)>>1
    if(arr[mid]<target):
        ans = mid+1
        low = mid+1
    else:
        high = mid-1
return count