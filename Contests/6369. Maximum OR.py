class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        
        def prefixOr(nums):
            prefix = [0]
            for i in range(len(nums)):
                prefix.append(prefix[-1] | nums[i])
            return prefix
        
        def suffixOr(nums):
            suffix = [0]
            for i in range(len(nums)-1, -1, -1):
                suffix.append(suffix[-1] | nums[i])
            return suffix[::-1]
        
        prefix = prefixOr(nums)
        suffix = suffixOr(nums)
        ans = -float('inf')
        for i in range(len(nums)):
            ans = max(ans, nums[i]*pow(2,k) | prefix[i-1] | suffix[i+1])
            print(ans, nums[i]*pow(2,k), prefix[i-1], suffix[i+1]
        
        return ans