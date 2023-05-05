class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
      i=0
      l=[]
      while(i<len(nums)-1):
        x = nums[i]
        y = nums[i+1]
        c = [y]*x
        l=l+c
        i+=2
      return l
    
        