t = int(input())
for _ in range(t):
  a,b = input().split()
  l = len(a)
  a = int(a,2)
  b = int(b,2)
  ans = a^b
  ans = bin(ans)[2:]
  if(len(ans)<l):
    count = l-len(ans)
    ans = "0"*count + ans
  print(ans)