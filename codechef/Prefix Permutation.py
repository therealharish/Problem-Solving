from functools import reduce
t = int(input())
for _ in range (t):
  n,l = map(int, input().split())
  l = list(map(int, input().split()))
  x=1;
  ans=[];
  for i in l:
    sub=[];
    for _ in range(i, x-1, -1):
      ans.append(_)
    x=i+1    
  print(*ans)
  