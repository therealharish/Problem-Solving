t = int(input())
for _ in range (t):
  size = int(input())
  n = list(map(int, input().split()))
  l = 0
  r = len(n)-1
  top = float('inf')
  flag = 1
  while(l<=r):
    if(max(n[l], n[r])<=top):
      if(n[l]>n[r]):
        top = n[l]
        l+=1
      else:
        top = n[r]
        r-=1
    elif(min(n[l], n[r])<=top):
      if(n[l]<n[r]):
        top = n[l]
        l+=1
      else:
        top = n[r]
        r-=1
    else:
      print("No")
      flag = 0
      break
  if(flag):
    print("Yes")
      