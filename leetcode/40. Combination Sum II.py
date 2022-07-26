#sliding window approach

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def tra(i, l, s, t):
          if(s==t):
              ans.append(l)
              return
          if(s>t):
              return
          for j in range(i, len(candidates)):
            if(j>i and candidates[j]==candidates[j-1]):
              continue
            tra(j+1, l+[candidates[j]], s+candidates[j], t)

        tra(0, [], 0, target)


        return ans
