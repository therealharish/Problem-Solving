t = int(input())
while(t):
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  c = list(map(int, input().split()))
  suma=sum(a)
  sumb=sum(b)
  sumc=sum(c)
  m=max(suma, sumb, sumc)
  print(m)
  t-=1