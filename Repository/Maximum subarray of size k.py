arr = [1,2,8,3,5,6,7,4]
prefix = [arr[0]]

for i in range(1, len(arr)):
  prefix.append(arr[i]+prefix[i-1])

maxSum = prefix[k-1]
index = k-1
for i in range(k, len(prefix)):
  sum = prefix[i]-prefix[i-k]
  if(maxSum>sum):
    index = i
    maxSum = sum
for i in range(index-k+1,index+1 ):
  print(arr[i], end="")
