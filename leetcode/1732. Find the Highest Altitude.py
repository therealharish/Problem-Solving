class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
      l = [0]
      for i in gain:
        l.append(i)
        
      for i in range(1, len(l)):
        l[i]=l[i]+l[i-1]

      return (max(l))
      