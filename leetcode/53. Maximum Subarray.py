class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
          if(nums[i-1]>0):
            nums[i]+=nums[i-1];
        return max(nums)
            
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
      ans = nums[0]
      currSum = 0
      for i in nums:
        if currSum < 0:
          currSum = 0
        currSum += i
        ans = max(ans, currSum)
      
      return ans