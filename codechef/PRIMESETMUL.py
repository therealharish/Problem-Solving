def pr(num):
  count=0;
  for i in range(1, num//2):
    if(num%i==0):
      count+=1;
  if(count==1):
    return True;
  else:
    return False;

t = int(input())
while(t):
  a = list(map(int, input().split()))
  s = list(map(int, input().split()))
  n=a[0]
  m=a[1]
  i=2;
  flag = 1;
  while(i<=m):
    l=[1];
    fa=1;
    for _ in range(1,i):
      if(pr(_) and _ in s):
        l.append(_)
    for _ in range(len(l)):
      if( _ not in s):
        fa = 0;
    if(fa):
      flag+=1
  print(flag)
  t-=1