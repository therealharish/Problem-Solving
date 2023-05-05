n = int(input())
while(n):
  l = int(input())
  if(l%2==0):
    d = l//2
    print(l+d)
  else:
    print(l+1)
  n=n-1;