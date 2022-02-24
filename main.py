import math
t = int(input())
for _ in range (t):
  b,c = map(int, input().split())
  g = math.gcd(c,b)
  a=c//g
  print(a)
  