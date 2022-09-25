class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      ws = 0
      maxL = 0
      maxF = 0
      d = {}
      for we in range(len(s)):
        d[s[we]] = d.get(s[we], 0) + 1
        maxF = max(d.values())
        maxL+=1
        if(maxL-maxF > k):
          d[s[ws]]-=1
          ws+=1
          maxL-=1
      return maxL
          
        
            
            
        
        
        