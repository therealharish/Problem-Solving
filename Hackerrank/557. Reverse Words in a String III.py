class Solution:
    def reverseWords(self, s: str) -> str:
      l = s.split(" ")
      newS = ""
      for i in s:
        news+=i[::-1]
      return newS