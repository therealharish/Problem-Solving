class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
      n = len(encoded)+1
      xorAll = 0
      for i in encoded:
        xorAll^=i
      foundXor = encoded[0]^encoded[-1]^xorAll
      xorExcludingFirstandLast = 0
      for i in range(1, len(encoded)-1):
        xorExcludingFirstandLast^=encoded[i]
      midElement = xorExcludingFirstandLast ^ foundXor
      print(midElement)

      midIndex = n//2
      perm = [0]*n
      perm[midIndex] = midElement
      i = midIndex-1
      j = midIndex+1
      while(i>=0 and j<n):
        print(perm)
        perm[i] = perm[i+1]^encoded[i]
        perm[j] = perm[j-1]^encoded[j]
        i-=1
        j+=1
      return perm
        
          
        