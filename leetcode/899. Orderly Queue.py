class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if(k>1):
            return "".join(sorted(s))
        else:
            ds = s+s
            ans = s
            n = len(s)
            for i in range(1, n):
                sub = ds[i:i+n]
                ans = min(ans, sub)
        return ans