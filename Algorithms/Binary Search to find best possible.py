while(left<right):
  mid = left+right//2
  if(arr[mid]==x):
    pos = mid
  if(arr[mid]>x):
    right = mid
  else:
    left = mid+1
    pos = left
