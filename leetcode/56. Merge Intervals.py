class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        prevInterval = intervals[0]
        for i in range(1,len(intervals)):
            currInterval = intervals[i]
            if(currInterval[0]<=prevInterval[1]):
                prevInterval[1] = max(prevInterval[1], currInterval[1])
            else:
                ans.append(prevInterval)
                prevInterval = currInterval.copy()
        ans.append(prevInterval)
        return ans
        
                