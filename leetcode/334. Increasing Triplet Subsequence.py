class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
      if(len(nums)<3):
        return False
      first = 2**31+1
      second = 2**31+1
      for i in range(len(nums)):
        print(first)
        if(first >= nums[i]):
          first = nums[i]
        elif(second >= nums[i]):
          second = nums[i]
        else:
          return True
      return False
      
        