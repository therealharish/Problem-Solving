class Solution:
    def nthUglyNumber(self, n: int) -> int:
      arr = [1]
      s = {1}
      i = 1
      while(len(s)<=1690):
        if(i*2 not in s):
          s.add(i*2)
          arr.append(i*2)
        if(i*3 not in s):
          s.add(i*3)
          arr.append(i*2)
        if(i*5 not in s):
          s.add(i*5)
          arr.append(i*2)
        while(i not in s):
          i+=1
      l = list(s)
      l.sort()
      print(l)
      return l[n-1]
        
      