m = 10**9 + 7

n, k = map(int, input().split())
str = input()

dp = [0] * (n + 1)
dp[n] = 1

for i in range(n - 1, -1, -1):
    if str[i] == '0':
        continue

    num = 0
    for j in range(i, n):
        num = num * 10 + int(str[j])
        if num > k:
            break
        dp[i] = (dp[i] + dp[j + 1]) % m

print(dp[0])
