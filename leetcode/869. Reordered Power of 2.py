class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
      
      noFreqCount = Counter(str(n))
      print(noFreqCount)
      l = []
      for i in range(32):
        l.append(Counter(str(2**i)))
      for i in range(len(l)):
        print(l[i])
        if(l[i]==noFreqCount):
          return True
      else:
        return False