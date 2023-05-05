class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      def convertToBase3(num):
        ans = ""
        while(num):
          ans=str(num%3)+ans
          num=num//3
        return ans

      n = convertToBase3(n)
      count = n.count("1")
      
      if(count == 1 and n[0]==1):
        return True
      else:
        return False