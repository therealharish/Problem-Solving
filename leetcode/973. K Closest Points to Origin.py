class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(k):
            x, y = points[i]
            dis = math.sqrt(x * x + y * y)
            heappush(maxHeap, (-dis, [x, y]))
        for i in range(k, len(points)):
            x, y = points[i]
            dis = math.sqrt(x * x + y * y)
            if (-maxHeap[0][0] > dis):
                heappop(maxHeap)
                heappush(maxHeap, (-dis, [x, y]))
        ans = []
        for i in range(k):
            ans.append(maxHeap[i][1])
        return ans
