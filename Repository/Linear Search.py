arr = [2.5,6,3,7,8,1,3]

# performing linear search
key = 6
p = -1
for i in range(len(arr)):
  if(arr[i] = key):
    p = i

if p == -1:
  print("Element not found!")
else:
  print("Element found at position: ", p)