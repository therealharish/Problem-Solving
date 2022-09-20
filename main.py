l = [2, 1, 6, -21, 7, 2, -1]
# l = [2,3,6,1,7,2,4]
dp = [-1]*len(l)
for i in range(len(l)-2, -1, -1):
  if(l[i]>dp[i+1] and l[i]>l[i+1]):
    dp[i] = -1
  elif(l[i]>dp[i+1] and l[i]<l[i+1]):
    dp[i] = l[i+1]
  elif(l[i]<dp[i+1] and l[i]<l[i+1]):
    dp[i] = l[i+1]
  else:
    dp[i] = dp[i+1]
print(dp)
    