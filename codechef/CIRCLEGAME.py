t = int(input())
while(t):
  a = list(map(int, input().split()))
  m=a[0]
  n=a[1]
  i=1;
  while(i<=n):
    l=[];
    for _ in range(1,i+1):
      l=l.append(_)
    if(len(l)<m):
      print(*l)
    
      
  t-=1