class Solution:
    def defangIPaddr(self, address: str) -> str:
      str = ""
      for i in address:
        if i == '.':
          str += "[.]"
        else:
          str+=i
      return str
          