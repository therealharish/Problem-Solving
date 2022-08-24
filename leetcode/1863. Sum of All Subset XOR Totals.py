class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
      n = len(nums)
      res = [[nums[k] for k in range(n) if i&1<<k] for i in range(2**n)]
      s = 0
      for i in res:
        xor=0
        for j in i:
          xor = xor^j
        s+=xor
      return s
        