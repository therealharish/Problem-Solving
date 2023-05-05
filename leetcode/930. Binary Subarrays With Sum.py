class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      d  = {}
      d[0] = 1
      prefixsum = 0
      ans = 0
      for i in nums:
        prefixsum+=i
        if(prefixsum - goal in d):
          ans+=d[prefixsum-goal]
        if(prefixsum in d):
          d[prefixsum]+=1
        else:
          d[prefixsum] = 1
      return ans