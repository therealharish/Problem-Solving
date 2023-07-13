class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def solve(i, s):
            if i == len(nums):
                if s == target:
                    return 1
                else:
                    return 0
            return solve(i + 1, s + nums[i]) + solve(i + 1, s - nums[i])
        return solve(0, 0)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def solve(i, s):
            if (i, s) in dp:
                return dp[(i, s)]
            if i == len(nums):
                if s == target:
                    return 1
                else:
                    return 0
            dp[(i, s)]  = solve(i + 1, s + nums[i]) + solve(i + 1, s - nums[i])
            return dp[(i, s)]
        return solve(0, 0)


