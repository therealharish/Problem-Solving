class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        s=""
        for i in jewels:
            if (i not in s and i in stones):
                count+=stones.count(i)
            s=s+i
        return count
            