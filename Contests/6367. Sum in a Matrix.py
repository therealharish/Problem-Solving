class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        for i in range(len(nums)):
            nums[i].sort()
        
        x = 0
        ans = 0
        while x < len(nums[0]):
            at = []
            for i in range(len(nums)):
                at.append(nums[i][x])
            ans += max(at)
            x+=1
            return ans
            
                