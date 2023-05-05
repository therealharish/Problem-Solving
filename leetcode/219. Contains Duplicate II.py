class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            curr = nums[i]
            if(curr in d):
                if((i-d[curr])<=k):
                    return True
                else:
                    d[curr] = i
            else:
                d[curr] = i
        return False
                
            