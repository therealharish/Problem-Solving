class Solution:
    def topKFrequent(self, nums: List[int], key: int) -> List[int]:
        d = Counter(nums)
        minHeap = []
        size = 0
        for k,v in d.items():
            if(size<key):
                heappush(minHeap, (v,k))
                size+=1
            else:
                if(minHeap[0][0]<v):
                    heappop(minHeap)
                    heappush(minHeap, (v,k))
        ans = []
        for i in range(key):
            ans.append(minHeap[i][1])
        return ans
            
                
            