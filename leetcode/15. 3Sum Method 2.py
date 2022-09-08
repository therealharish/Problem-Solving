# in notes pg 10
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def findPair(nums, start, target, res):
            end = len(nums) - 1
            while (start < end):
                currSum = nums[start] + nums[end]
                if (currSum == target):
                    res.append([-target, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while (start < end and nums[start] == nums[start - 1]):
                        start += 1
                    while (start < end and nums[end] == nums[end + 1]):
                        end -= 1
                elif (currSum < target):
                    start += 1
                else:
                    end -= 1
        
        res = []
        nums.sort()
        print(nums)
        
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            target = -nums[i]
            findPair(nums, i + 1, target, res)
        return res
