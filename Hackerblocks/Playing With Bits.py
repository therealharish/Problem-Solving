t = int(input())
for _ in range (t):
  a,b = map(int, input().split())
  ans = 0
  for i in range(a, b+1):
    count = bin(i).count("1")
    ans+=count
  print(ans)