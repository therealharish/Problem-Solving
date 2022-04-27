class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      s = ""
      for i in digits:
        s+=str(i)
      print(s)
      s=int(s)
      s+=1
      s=str(s)
      l = []
      l[:0] = s
      return l
      