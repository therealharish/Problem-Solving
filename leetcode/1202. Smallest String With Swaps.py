class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
      def swap(x, y, s):
        news=""
        for i in range(len(s)):
          if(i==x):
            news+=s[y]
          elif(i==y):
            news+=s[x]
          else:
            news+=s[i]
        return news

      for i in pairs:
        a,b = i
        s=swap(a,b,s)
      return s