arr = [2,3,6,3,2]
ans = [0 for i in range(len(arr))]
mi = min(arr)
ma = max(arr)
count = [0 for i in range(mi, ma+=1)]

for i in range(mi, ma+1):
  count(arr[i])+=1

print(count)