class Solution:
    def sortColors(self, nums: List[int]) -> None:
      x = nums.count(0)
      y = nums.count(1)
      z = nums.count(2)
      xx = [0]*x
      yy = [1]*y
      zz = [2]*z

      xx.extend(yy)
      xx.extend(zz)

      nums[:] = xx
    