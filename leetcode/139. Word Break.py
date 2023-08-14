class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def solve(i):
            if i >= len(s):
                return True
            for j in wordDict:
                if s[i:].startswith(j):
                    return solve(i+len(j))
                    
        return solve(0)