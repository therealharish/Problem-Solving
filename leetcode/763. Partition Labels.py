class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        startingindex = 0
        l = []
        posans = 0
        charans = len(s)-1

        dictdp = {}
        for i in range(len(s)):
          dictdp[s[i]] = s.rindex(s[i])
        for i in range(len(s)):
          start = i
          end = len(s)-1
          if(posans < dictdp[s[i]]):
            posans = dictdp[s[i]]
          if(i == posans):
            l.append(posans-startingindex+1)
            startingindex = posans+1

        return l