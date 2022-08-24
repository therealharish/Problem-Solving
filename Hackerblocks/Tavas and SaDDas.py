n = input()
l = len(n)
ans = 2**l - 2
for i in range(l-1, -1, -1):
  if(n[i]=='7'):
    ans+=(2**(l-i-1))
print(ans)

