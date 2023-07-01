# backtracking
class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        
        d = Counter(tiles)
        ans = set()
        def solve(s, d):
            
            for i in d:
                if d[i] > 0:
                    d[i] -= 1
                    ans.add(s+i)
                    solve(s+i, d)
                    d[i] += 1
        
        solve("", d)
        return len(ans)

# better backtracking
class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        
        d = Counter(tiles)
        ans = 0
        def solve(d):
            nonlocal ans
            for i in d:
                if d[i] > 0:
                    d[i] -= 1
                    ans += 1
                    solve(d)
                    d[i] += 1
        
        solve(d)
        return ans
    
# head recursion
class Solution3:
    def numTilePossibilities(self, tiles: str) -> int:
        
        d = Counter(tiles)
        
        
        def solve(d):
            
            count = 1
            for i in d:
                if d[i] > 0:
                    d[i] -= 1
                    count += solve(d)
                    d[i] += 1
                    
            return count
        
        return solve(d) - 1 
    
    
# head recursion 2
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        d = [0 for _ in range(26)]
        
        for i in tiles:
            d[ord(i) - ord('A')] += 1
            
        @cache
        def solve(d):
            
            count = 1
            for i in range(26):
                if d[i] > 0:
                    d[i] -= 1
                    count += solve(d)
                    d[i] += 1
                
        return solve(d) - 1 
            
            
            
        
        