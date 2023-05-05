class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
      ans = []
      def tra(i, l, s, t):
        print(l)
        if(s==t):
            ans.append(l)
            return
        if(s>t):
            return
        for j in range(i, len(candidates)):
          tra(j, l+[candidates[j]], s+candidates[j], t)

      tra(0, [], 0, target)
      

      return ans
            