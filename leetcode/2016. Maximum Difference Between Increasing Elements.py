class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
      l=[]
      for i in range(len(nums)):
        for j in range(i):
          if(nums[j]<nums[i] and j<i):
            l.append(nums[i]-nums[j])
          if(nums[j]>nums[i] and j>i):
            l.append(nums[j]-nums[i])
      return max(l)