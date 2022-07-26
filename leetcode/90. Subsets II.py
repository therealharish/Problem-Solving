class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recur(ind, l, ans):
            ans.append(l[:])
            for i in range(ind, len(nums)):
                if (i != ind and nums[i] == nums[i - 1]):
                    continue
                l.append(nums[i])
                recur(i + 1, l, ans)
                l.pop(-1)

        nums.sort()
        recur(0, [], ans)

        return ans