class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      ans = []
      count = 0
      memo = [1]*len(nums)
      best = 1
      for i in range(len(nums)):
        m = 1
        for j in range(i):
          if(nums[i]>nums[j]):
            if(best == m):
              count+=1
            if(m<memo[j]):
              m = memo[j]
              if(best < m):
                best = m
                count=1
        memo[i] = m+1
      return count

            