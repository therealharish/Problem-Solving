class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
      k = 1
      count=0
      while(True):
        if(n-(k*(k-1)/2)):
          if((n-k*(k-1))/2%2==0):
            count+=1
          k+=1
        else:
          break
      return count
      