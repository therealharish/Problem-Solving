class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
      dup = nums.copy()
      nums  = set(nums)
      s=0
      for i in nums:
        s+=(i*2)
      return s-sum(dup)