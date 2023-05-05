t = int(input())
while(t):
  d = list(map(int, input().split()))
  s = list(map(int, input().split()))
  x= d[1];
  s.sort(reverse=True)
  sum = 0;
  count=0;
  while(len(s) and sum<x):
    sum+=s.pop(0);
    count+=1
  if(sum>=x):
    print(count)
  else:
    print("-1")
    
  
      
  t-=1