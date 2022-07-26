sieve = [True for i in range(100)]
for i in range(2, len(sieve)):
  p = i**2
  while(p<len(sieve)):
    sieve[p]=False
    p+=i

dp = [0 for i in range(len(sieve))]
count = 0
for i in range(2, len(sieve)):
  if(sieve[i] == True):
    dp[i] = dp[i-1]+1
  else:
    dp[i] = dp[i-1]
print(dp)

dpofpc = [0 for i in range(len(dp))]
for i in range(2, len(dp)):
  if(sieve[dp[i]] == True):
    dpofpc[i] = dpofpc[i-1]+1
  else:
    dpofpc[i] = dpofpc[i-1]
print(dpofpc)

t = int(input())
for _ in range(t):
  n,m = map(int, input().split())
  print(dpofpc[m]-dpofpc[n])




