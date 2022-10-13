class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
      ws = 0
      ans = float('inf')
      remove = 0
      for we in range(len(blocks)):
        windowLength = we-ws+1
        curr = blocks[we]
        if(curr == "W"):
          remove+=1
        if(windowLength == k):
          ans = min(ans, remove)
          if(blocks[ws]=="W"):
            remove-=1
          ws+=1
      return ans
        
        