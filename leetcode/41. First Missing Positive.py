class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      n = len(nums)
      # change any negative or zero number to out of range because logically it shouldn't contribute in our hashmap
      for i in range(len(nums)):
        if(nums[i]<=0):
          nums[i]=n+1
      for i in range(len(nums)):
        x = abs(nums[i])
        if(x>len(nums)):
          continue
        else:
          if(nums[x-1]>0):
            nums[x-1]*=-1
      for i in range(len(nums)):
        if nums[i]>0:
          return i+1
      return n+1