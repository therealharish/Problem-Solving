from math import ceil

def solve(s):
    newS = ""
    i = 0
    while (i < len(s)):
        newS += s[i]
        j = i
        while (i < len(s) and s[i] == s[j]):
            i += 1
    return ceil((len(newS) + 1) / 2)

s = input()
# print(solve(s))

def findMinimumDeletion(l, r, dp, s):
 
    if l > r:
        return 0
    if l == r:
        return 1
    if dp[l][r] != -1:
        return dp[l][r]
 
    # When a single character is deleted
    res = 1 + findMinimumDeletion(l + 1, r,
                                     dp, s)
 
    # When a group of consecutive characters
    # are deleted if any of them matches
    for i in range(l + 1, r + 1):
 
        # When both the characters are same then
        # delete the letters in between them
        if s[l] == s[i]:
            res = min(res, findMinimumDeletion(l + 1, i - 1, dp, s) +
                           findMinimumDeletion(i, r, dp, s))
     
    # Memoize
    dp[l][r] = res
    return res

print(findMinimumDeletion(0, len(s) - 1, [[-1 for i in range(len(s))] for j in range(len(s))], s))


            

