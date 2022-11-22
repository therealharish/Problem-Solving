class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def findMerge(l):
            prev = l[0]
            curr = l[1]
            merge = []
            merge.append(min(prev[1], curr[0]))
            merge.append(min(prev[1], curr[1]))
            return merge
		
        areaA = abs(ax1-ax2)*abs(ay1-ay2)
        areaB = abs(bx1-bx2)*abs(by1-by2)
        lA = [[min(ax1, ax2), max(ax1, ax2)], [min(bx1, bx2), max(bx1, bx2)]]
        lB = [[min(ay1, ay2), max(ay1, ay2)], [min(by1, by2), max(by1, by2)]]
        lA.sort()
        lB.sort()
        x = findMerge(lA)
        x = x[1]-x[0]
        y = findMerge(lB)
        y = y[1]-y[0]
        mergeArea = x*y
        area = areaA+areaB-mergeArea
        print(x)
        return area
        