class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
      l = []
      for i in paths:
        l.append(i.split(" "))
      d = {}
      for i in l:
        dir = i[0]
        for j in i[1:]:
          content = j.split(".txt")
          if(content[1] in d):
            d[content[1]].append((dir, content[0]))
          else:
            d[content[1]] = [(dir, content[0])]
      ans = []
        
      for x,y in d.items():
        same = []
        if(len(y)>1):
          for i in y:
            same.append(i[0]+"/"+i[1]+".txt")
        if(same):
            ans.append(same)

      return ans
            
        
            
          
        