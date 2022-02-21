class Solution:
    def numberOfMatches(self, n: int) -> int:
      count = 0;
      o=n;
      while (n>0):
        n=n//2
        count+=o-n
        o=n
      return count