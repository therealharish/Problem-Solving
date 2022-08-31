class Solution:
    def nearestPalindromic(self, n: str) -> str:
      
        if(len(n)&1):
          first = n[:len(n)//2+1]
          second = n[len(n)//2+1:]
          print(first, second)

          f = len(first)
          s = len(second)
          s1 = first+first[0:f-1][::-1]
          s = first[:f-1]+str(int(first[f-1])+1)+first[:f-1][::-1]
          if(abs(int(s1)-int(n)) < abs(int(s))-int(n)):
            res = s1
          else:
            res = s
          return res

        else:
          first = n[:len(n)//2]
          second = n[len(n)//2:]
          f = len(first)
          s = len(second)
          s1 = first+first[::-1]
          s = first[0:f-1]+str(int(first[f-1])+1)+str(int(first[f-1])+1)+ first[:f-1][::-1]
          if(abs(int(s1)-int(n)) < abs(int(s))-int(n)):
            res = s1
          else:
            res = s
          return(res)
