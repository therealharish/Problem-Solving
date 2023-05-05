class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        fullsum = sum(nums)
        lsum = 0
        lcount = 0
        rsum = 0
        rcount = 0
        for i in range(len(nums)):
          rsum = fullsum - lsum - nums[i]
          rcount = len(nums) - lcount - 1
          s = (nums[i]*lcount - lsum) + (rsum - nums[i]*rcount)
          ans.append(s)
          lsum+= nums[i]
          lcount+=1
        return ans