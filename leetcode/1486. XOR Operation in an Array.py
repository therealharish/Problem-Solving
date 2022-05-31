class Solution:
    def xorOperation(self, n: int, start: int) -> int:
      l = []
      for i in range(n):
        l.append(start + 2*i)
      xor = start
      for i in range(1, len(l)):
        xor^=i
      return xor
        
        