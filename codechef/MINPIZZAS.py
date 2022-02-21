import math
n = int(input())


while(n):
  i=1;
  l = list(map(int, input().split()))
  while(i):
    need = str((l[1]*i)/l[0])
    if(need[-1]=='0'):
     print(i)
     break;
    else:
      i=i+1

  n=n-1;