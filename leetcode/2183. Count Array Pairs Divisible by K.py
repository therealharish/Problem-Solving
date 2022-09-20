# in notes 1 pg 

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
      
      def gcd(a, b):
        if(b==0):
          return a
        else:
          return gcd(b, a%b)

      d = {}
      ans = 0
      
      for i in nums:
        n = gcd(k, i)
        for x,y in d.items():
          if((n*x)%k==0):
            ans+=y
        if(n in d):
          d[n]+=1
        else:
          d[n]=1

      return ans
        