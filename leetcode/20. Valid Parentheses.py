class Solution:
    def isValid(self, s: str) -> bool:
      l=[]
      if(len(s)==1):
        return False
      for i in s:
        if(len(l)==0):
          l.append(i)
        else:
          if(l[-1]=="(" and i==")"):
            l.pop(-1)
          elif(l[-1]=="[" and i=="]"):
            l.pop(-1)
          elif(l[-1]=="{" and i=="}"):
            l.pop(-1)
          else:
            l.append(i)
          
      if(len(l)==0):
        return True
      else:
        return False