# in notes 1 pg 36
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws, we = 0,0
        maxLen = 0
        d = {}
        for we in range(len(s)):
            char = s[we]
            if(char in d and d[char]>=ws):
                ws = d[char]+1
                d[char] = we
            else:
                d[char] = we
                maxLen = max(maxLen, we-ws+1)
        return maxLen
