# Missing Ranges
# Data Stream as Disjoint Intervals
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
      l=[]
      if(len(nums)==0):
        return []
      x=nums[0]
      newl=[]
      i=0;
      while(i<len(nums)):
        if(x==nums[i]):
          newl.append(x)
          x+=1
          i+=1
        else:
          x=nums[i]
          l.append(newl)
          newl=[]
    
      l.append(newl)
      ans = []
      for i in l:
        s=""
        if(len(i)==1):
          s=str(i[0])
          ans.append(s)
        else:
          s=str(i[0])+"->"+str(i[-1])
          ans.append(s)
        
      
      
      return ans
      
        
      