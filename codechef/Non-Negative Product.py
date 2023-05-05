t = int(input())
for _ in range (t):
  size = int(input())
  arr = list(map(int, input().split()))
  if(0 in arr):
    print(0)
    break 
  count = 0
  for i in arr:
    if(i<0):
      count+=1 
          
  if(count%2 == 0):
    print(0)
    break
  else:
    print(1)
    break
  if(count == 0):
    print(count)
    