# will get TLE
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(nums, n):
            if (n == 0):
                return
            maxIndex = findMaxIndex(nums, n)
            nums[maxIndex], nums[n - 1] = nums[n - 1], nums[maxIndex]
            sort(nums, n - 1)

        def findMaxIndex(nums, n):
            f = max(nums[:n])
            i = nums[:n].index(f)
            return i

        sort(nums, len(nums))
        return nums
