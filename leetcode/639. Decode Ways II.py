class Solution:
    def numDecodings(self, s: str) -> int:
        
        d = {
            '*': 9,
            '*0': 2,
            '*1': 2,
            '*2': 2,
            '*3': 2,
            '*4': 2,
            '*5': 2,
            '*6': 2,
            '*7': 1,
            '*8': 1,
            '*9': 1,
            '**': 15,
            '1*': 9,
            '2*': 6,
            '3*': 0,
            '4*': 0,
            '5*': 0,
            '6*': 0,
            '7*': 0,
            '8*': 0,
            '9*': 0,
        }
        
        @cache
        def solve(i):
            if i == len(s):
                return 1
            if s[i] == 0:
                return 0
            
            # single digit
            if s[i] == '*':
                left = 9 * solve(i+1)
            else:
                left = solve(i+1)
                
            # double digit
            if i+1 < len(s):
                curr = s[i:i+2]
                if curr in d:
                    right = d[curr] * solve(i+2)
                else:
                    right = solve(i+2)
            else:
                right = 0
            
            print(s[i], left, curr, right)
            return (left + right) % (10**9 + 7)
        
        return solve(0)
            
        
        