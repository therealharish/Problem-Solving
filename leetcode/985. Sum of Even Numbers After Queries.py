class Solution:
    def sumEvenAfterQueries(self, nums: List[int],
                            queries: List[List[int]]) -> List[int]:
        evenSum = 0

        for i in nums:
            if (not i & 1):
                evenSum += i

        ans = []

        for i in range(len(queries)):

            query = queries[i]

            if (nums[query[1]] % 2 == 0):
                evenSum -= nums[query[1]]

            nums[query[1]] += query[0]

            if (nums[query[1]] % 2 == 0):
                evenSum += nums[query[1]]

            ans.append(evenSum)

        return ans
