class Solution:
    def reverseWords(self, s: str) -> str:
      l = s.split(" ")
      str = ""
      for i in l:
        str+=i[::-1]
        str+=" "

      return str.strip()
      