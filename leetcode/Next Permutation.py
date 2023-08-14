class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =  len(nums) - 2
        while (i >= 0 and nums[i] >= nums[i + 1]):
            i -= 1
        print(i)
        if i == -1:
            nums = nums.reverse()
        else:
            j = len(nums) - 1
            while (j > i and nums[j] <= nums[i]):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = sorted(nums[i + 1:])