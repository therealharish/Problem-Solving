import heapq
arr = [12, 4, 5, 3, 8, 7]
minheap = []
maxheap = []
heapq.heapify(minheap)
heapq.heapify(maxheap)

for i in arr:
  heapq.heappush(maxheap, -i)
  heapq.heappush(minheap, -heapq.heappop(maxheap))

  if(len(minheap)>len(maxheap)):
    heapq.heappush(maxheap, -heapq.heappop(minheap))

  if(len(minheap) == len(maxheap)):
    print((minheap[0]-maxheap[0])/2)
  else:
    print(-maxheap[0])