class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recur(pos):
            if(pos>=len(nums)):
                memo[pos] = 0
                return 0
            if pos in memo:
                return memo[pos]
            memo[pos] = max(nums[pos]+recur(pos+2), recur(pos+1))
            return memo[pos]
        return recur(0)