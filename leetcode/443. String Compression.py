class Solution:
    def compress(self, chars: List[str]) -> int:
      i=0  
      l=0
      if(len(chars)==1):
        return 1
      while(i<len(chars)):
        x = chars[i]
        ptr = i
        count=0
        while(ptr<len(chars) and x==chars[ptr]):
          ptr+=1
          count+=1
        if(count == 1):
          l+=1
          i=ptr
          continue
        else:
          if(count>9):
            count=str(count)
            for item in count:
              chars[i+1]=str(item)
              i+=1
              l+=1
            l+=1
          else:
            chars[i+1] = str(count)
            l+=2
        i=ptr
      return l
          
          