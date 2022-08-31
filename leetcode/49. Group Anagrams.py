class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
      d = {}
      for i in strs:
        present = tuple(Counter(i))
        if(present in d):
          d[present].append(i)
        else:
          d[present] = i
      return d.values()
      