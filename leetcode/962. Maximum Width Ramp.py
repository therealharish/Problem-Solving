# in notes 1 pg 35
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
      res = 0
      arr = []
      for i in range(len(nums)):
        right = len(arr)-1
        if not arr:
          arr.append(i)
          continue
        if(nums[i] >= nums[arr[-1]]):
          while(right > -1 and nums[i]>= nums[arr[right]]):
            res = max(res, i-arr[right])
            right -= 1
        else:
          arr.append(i)
      return res
          
          