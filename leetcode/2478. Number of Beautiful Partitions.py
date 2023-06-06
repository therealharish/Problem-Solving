class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        coprime = ['1', '4', '6', '8', '9']
        def solve(i, count):
            
            if s[i] in coprime:
                return 0
            
            if count >= k:
                return 0
            
            if i == len(s):
                if count == k:
                    return 1
                else:
                    return 0
                
            p = 0
            for j in range(i + minLength-1, len(s)):
                if s[j] in coprime:
                    p += solve(j+1, count+1)
            return p
        
        return solve(0, 0)
            