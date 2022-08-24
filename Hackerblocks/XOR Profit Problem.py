a = int(input())
b = int(input())
ans = -10000
for i in range(a,b+1):
  for j in range(a, b+1):
    ans = max(ans, i^j)
print(ans)