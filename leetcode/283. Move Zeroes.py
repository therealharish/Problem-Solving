class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      n = nums
      c = n.count(0)
      for i in range(c):
        n.remove(0)
      l = [0]*c
      n.extend(l)
      nums[:] = n
        