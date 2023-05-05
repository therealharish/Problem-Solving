arr = [2.5,6,3,7,8,1,3]

# performing linear search
key = 6
p = -1
arr.sort()
print(arr)
l = 0
h = len(arr)-1
while(l<=h):
  mid = (l+h)//2
  if(arr[mid] == key):
    p = mid
    break
  elif(arr[mid]>key):
    h = mid-1
  elif(arr[mid]<key):
    l = mid+1

    

if p == -1:
  print("Element not found!")
else:
  print("Element found at position: ", p)