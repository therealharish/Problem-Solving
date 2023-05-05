class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        d = Counter(changed)
        ans = []
        if (len(changed) & 1):
            return []
        for i in changed:
            if (i == 0 and d[i] > 0):
                ans.append(i)
                d[i] -= 2
            if d[i] > 0 and d[i * 2] > 0:
                ans.append(i)
                d[i] -= 1
                d[i * 2] -= 1
        for x, y in d.items():
            if y > 0:
                return []
        return ans
