from math import *

arr = [19, 56, 28, 20, 14, 1, 11, 7, 5, 3]
arr = [8,3,9,12,15]
dp = [0]*len(arr)
dp[0] = 1
for i in range(1, len(arr)):
    dp[i]=dp[i-1]+1
    j = 0
    while(j<i):
        if(gcd(arr[i], arr[j])>1):
            if(j>0):
                dp[i] = dp[j-1]+1
            else:
                dp[i] = dp[j]
                
            break
        j+=1
print(dp)
print(dp[-1])

            
    
    
    