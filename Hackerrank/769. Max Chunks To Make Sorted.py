class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
      chunk = 0
      window = 0
      for i in range(len(arr)):
        window = max(window, arr[i])
        if(i==window):
          chunk+=1
      return chunk
        
          

        
      
          
        
      
        