class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      s = set(nums)
      ans = 0
      for i in nums:
        seq = 0
        if((i-1) not in s):
          j = i
          while(j in s):
            seq+=1
            j+=1
        ans = max(ans, seq)
      return ans
          
          
          