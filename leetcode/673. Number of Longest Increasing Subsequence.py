class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      ans = []
      lis = [1]*len(nums)
      count = [1]*len(nums)
      for i in range(1, len(nums)):
        for j in range(i):
          if(nums[i]>nums[j] and lis[j]+1>lis[i]):
            lis[i] = lis[j]+1
            count[i] = count[j]
          elif(nums[i]>nums[j] and lis[j]+1==lis[i]):
            count[i] = count[j] + 1
      ans = 0
      best = max(lis)
      print(lis)
      for i in range(len(lis)):
        if(nums[i]==best):
          ans+=count[i]
      return ans

            