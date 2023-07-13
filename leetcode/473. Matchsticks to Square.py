class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        set = [0] * 4
        matchsticks.sort(reverse=True)
        
        def solve(index, set, answer):
            if index == len(matchsticks):
                if set[0] == set[1] == set[2] == set[3]:
                    answer =  True
                else:
                    a = matchsticks[index]
                    solve(index + 1,set[0]+a, answer)
                    solve(index + 1,set[1]+a, answer)
                    solve(index + 1,set[2]+a, answer)
                    solve(index + 1,set[3]+a, answer)
            return answer
        return solve(0, set, False)
                    