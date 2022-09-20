
class Solution:
    def longestKSubstr(self, s, k):
        if (len(s) < k):
            return -1
        d = {}
        ws = 0
        we = 0
        maxLen = -1
        for we in range(len(s)):
            char = s[we]

            d[char] = d.get(char, 0) + 1

            if (len(d) == k):
                maxLen = max(maxLen, we - ws + 1)
            else:
                while (len(d) > k):
                    removeChar = s[ws]
                    d[removeChar] -= 1
                    if (d[removeChar] == 0):
                        del d[removeChar]
                    ws += 1
        return maxLen
