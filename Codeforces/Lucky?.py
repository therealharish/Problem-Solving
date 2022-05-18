t = int(input())
for _ in range(t):
  n = input()
  x = int(n[0]) + int(n[1]) + int(n[2])
  y = int(n[-1]) + int(n[-2]) + int(n[-3])
  if(x==y):
    print("YES")
  else:
    print("NO")