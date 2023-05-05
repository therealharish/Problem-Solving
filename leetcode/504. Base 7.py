class Solution:
    def convertToBase7(self, num: int) -> str:
      s=""
      if(num == 0):
        return '0'
      if(num<0):
        num=0-num
        flag = 1
      while(num):
        s+=str(num%7)
        num = num//7
      if(flag):
        s+='-'
      return s[::-1]