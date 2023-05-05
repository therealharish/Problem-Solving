l = [2,5,3,7,8,1,9]
# l=[5,7,4,9,8,10]
c = []
s=[]
i=0;
for i in range(len(l)):
  s = l[i+1:]
  flag=1
  while(s):
    if(s[0]>l[i]):
      c.append(s[0])
      flag=0
      break;
    else:
      s.pop(0)
  if(flag):
    c.append(-1)
print(c)

# Method 2

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

