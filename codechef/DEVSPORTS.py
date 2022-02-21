t = int(input())
while(t):
  n = list(map(int, input().split()))
  left = n[0]-n[1];
  required = n[2]+n[3]+n[4];
  if (left >= required):
    print("YES")
  else:
    print("NO")
  t-=1