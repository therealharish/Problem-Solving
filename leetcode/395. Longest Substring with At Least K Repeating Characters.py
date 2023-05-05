class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
      i,j = 1, len(s)-1
      count = 0
      while(i<=j):
        if(s[i] == s[i-1]):
          count+=1
        else:
          count = 0
        if(count == k):
          return True
        i+=1
        j+=1
      return False
        