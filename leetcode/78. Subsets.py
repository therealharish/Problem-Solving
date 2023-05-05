class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      s=[[]]
      ssize = int(math.pow(len(nums)))
      counter = 0
      j=0
      for counter in range(0, ssize):
        l=[]
        for j in range(0, len(nums)):
          if((counter and (1<<j))>0):
            l.append(j)
        s.append(l)
      return s
        