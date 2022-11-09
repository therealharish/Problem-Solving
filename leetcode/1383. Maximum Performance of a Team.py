class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = []
        for i in range(len(efficiency)):
            arr.append((efficiency[i], speed[i]))
        arr.sort(reverse = True)
        s = 0
        res = 0
        minHeap = []
        for i in range(k):
            s += arr[i][1]
            res = max(res, s*arr[i][0])
            heappush(minHeap, arr[i][1])
        for i in range(k, len(arr)):
            pop = heappop(minHeap)
            s-=pop
            s+=arr[i][1]
            res = max(res, s*arr[i][0])
            heappush(minHeap, arr[i][1])

        return res % (10**9+7)
			
			
					
            
        