class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
      st = set()
      for i in range(len(s)):
        if len(st[i:i+k])==k: 
          st.add(s[i:i+k])
      if(len(st) == 2**k):
        return True
      else:
        return False