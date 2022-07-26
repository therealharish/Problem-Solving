arr = [ 1, 3, 3, 4 ]
x = 3
first = -1
last = -1
low, high = 0, len(arr)-1
while(low<=high):
  mid = (low+high)//2
  if(arr[mid]==x):
    if(mid == 0):
      first = mid
    else:
      if(arr[mid-1]<x):
        first = mid
  if(arr[mid]<x):
    low = mid+1
  else:
    high = mid-1
print(first)
