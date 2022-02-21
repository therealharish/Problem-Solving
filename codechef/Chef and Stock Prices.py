n = int(input())

while(n):
  l = map(int, input().split())
  new = l[0]+l[0]*l[3]/100
  if(new>=l[1] or new <= l[2]):
    print("YES")
  else:
    print("NO");
  n=n-1;
