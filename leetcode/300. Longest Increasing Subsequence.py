# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#       dp = [1]*len(nums)
#       for i in range(len(nums)-1, -1, -1):
#         for j in range(i+1, len(nums)):
#           if(nums[j]>nums[i]):
#             dp[i] = max(1+dp[j], dp[i])
#       return max(dp)

# in notes 1 page 3
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#       ans = 0
#       m = 0
#       memo = [0]*len(nums)
#       for i in range(len(nums)):
#         for j in range(i):
#           if(nums[i]>nums[j] and m<memo[j]):
#             m = memo[j]
#         memo[i] = m+1
#         ans = max(ans, memo[i])
#       return ans


# in notes 1  pg 5 method 2
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		ans = []

		def binarysearch(low, high, target):
			mid = (low + high) // 2
			if (low >= high):
				return low
			if (ans[mid] == target):
				return mid
			elif (ans[mid] > target):
				binarysearch(low, mid - 1)
			else:
				binarysearch(mid, high)

		for i in nums:
			if (len(ans) == 0):
				ans.append(i)
			else:
				if (i > ans[-1]):
					ans.append(i)
				else:
					pos = binarysearch(0, len(arr) - 1, i)
					ans[pos] = i
		return len(ans)
