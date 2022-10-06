class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 1
        timePrev = 0
        prev = ""
        for i in range(len(colors)):
            curr = colors[i]
            if (curr == prev):
                if (timePrev < neededTime[i]):
                    ans += timePrev
                    timePrev = neededTime[i]
                else:
                    ans += neededTime[i]
            else:
                prev = curr
                timePrev = neededTime[i]
        return ans
