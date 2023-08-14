s = input()

def solve(s):
    ans = 0
    re = s[::-1]
    for i in range(len(s)):
        if s[i] == re[i]:
            ans += 1
    return ans

print(solve(s))