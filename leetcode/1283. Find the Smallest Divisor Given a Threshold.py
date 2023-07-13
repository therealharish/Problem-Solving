class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        nums.sort()
        low = 1
        high = max(nums)
        
        def validate(divisor):
            
            s = 0
            for i in nums:
                s += ceil(i / divisor)
            return s <= threshold
            
        
        while (low < high):
            mid = (low + high) // 2
            if validate(mid):
                high = mid
            else:
                low = mid + 1
        return high
    