arr = [7,5,6,11,14,15,11,6]
xo = 0
for i in range(1, len(arr)-1):
  print(arr[i])
  xo^=arr[i]
print(xo)