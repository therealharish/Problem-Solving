class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        p = 0
        q = 0
        ans = []
        while (p < len(firstList) and q < len(secondList)):
            start = max(firstList[p][0], secondList[q][0])
            end = min(firstList[p][1], secondList[q][1])
            if (start <= end):
                ans.append([start, end])
            if (firstList[p][1] < secondList[q][1]):
                p += 1
            else:
                q += 1
        return ans
