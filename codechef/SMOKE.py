import math

t = int(input())
for _ in range (t):
  n,x,y = map(int, input().split())
  if(n>100):
    bus = math.ceil(n//100)
    n = n%x
    car = math.ceil(n//4)
    buscost = bus*x + car*y
  else:
    car = math.ceil(n//4)
    carcost = car*y
  print(cost)
    
  