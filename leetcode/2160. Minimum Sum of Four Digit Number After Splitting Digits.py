class Solution:
    def minimumSum(self, num: int) -> int:
      num = str(num)
      l = list(num)
      l.sort()
      i = 0
      j = len(l)-1
      su =0
      while(i<=j):
        s1 = str(l[i])+str(l[j])
        su += int(s1)
        i+=1
        j-=1
      return su 