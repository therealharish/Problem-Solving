class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      maxnum = 1
      minnum = 1
      res = -1e9
      for i in nums:
        if(i<0):
          maxnums, minnum = minnum, maxnum
        maxnum = max(maxnum*i, i)
        minnum = min(minnum, i)

        res  = max(res, maxnum)
        if(maxnum==0):
          maxnum = 1
        if(minnum == 0):
          minnum = 1
      return res