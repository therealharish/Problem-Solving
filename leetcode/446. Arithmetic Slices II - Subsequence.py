class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count=0
        dp = [{} for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                jCount = 0
                iCount = 0
                if diff in dp[j]:
                    jCount = dp[j][diff]
                if diff in dp[i]:
                    iCount = dp[i][diff]
                count+=jCount
                dp[i][diff] = jCount+iCount+1    
        return count
                    
                    
            