class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if(len(intervals)==0):
            return [newInterval]
        
        for i in range(len(intervals)):
            currInterval = intervals[i]
            if(newInterval[1] < currInterval[0]):
                res.append(newInterval)
                return res+intervals[i:]
            elif(newInterval[0]>currInterval[1]):
                res.append(currInterval)
            else:
                newInterval[0] = min(currInterval[0], newInterval[0])
                newInterval[1] = max(currInterval[1], newInterval[1])
        
        res.append(newInterval)
        return res
                
            
        