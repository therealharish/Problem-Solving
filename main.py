from heapq import heappush, heappop
from collections import Counter
def rs(s,k):
        d = Counter(s)
        maxHeap = []
        for key,v in d.items():
            heappush(maxHeap, [-v,key])
        ans = ""
        queue = [] 
        while(maxHeap):
            freq, char = heappop(maxHeap)
            ans+=char
            freq+=1
            queue.append([freq, char])
            
            if(len(queue)==k):
                element = queue.pop(0)
                if(-element[0]>0):
                  heappush(maxHeap, element)
            print(maxHeap, ans)
          
        if(len(ans)!=len(s)):
            return ""
        else:
            return ans

print(rs("aaadbbcc", 2))
