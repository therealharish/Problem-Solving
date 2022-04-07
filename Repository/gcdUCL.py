import sys


def gcd(a,b):
  if(a>b):
    return b
  else:
    return gcd(b, a%b)

x,y = sys.argv[0], sys.argv[1:]

y = list(map(int, y))
print(x)
print(y)

g = gcd(y[0], y[1])
print(g)