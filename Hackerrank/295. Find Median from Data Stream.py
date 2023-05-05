class MedianFinder:

    def __init__(self):
		self.minHeap = minHeap
		self.maxHeap = maxHeap
        

    def addNum(self, num: int) -> None:
        minHeap = self.minHeap
		maxHeap = self.maxHeap
		heappush(maxHeap, -num)
		if(len(maxHeap)>len(maxHeap)):
			ele = -heappop(minHeap)
			heappush(minHeap, ele)
		if(minHeap and minHeap[0] < (-maxHeap[0])):
			# eleMax = -heappop(maxHeap)
			ele = -heappop(maxHeap)
			heappush(maxHeap, ele)
			# heappush(minHeap, eleMax)
		print(minHeap, maxHeap)
		

    def findMedian(self) -> float:
		minHeap = self.minHeap
		maxHeap = self.maxHeap
		if((len(maxHeap)+len(minHeap))%2==0):
			return (maxHeap[0]+minHeap[0])/2
		else:
			return maxHeap[0]
		
		
		
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()