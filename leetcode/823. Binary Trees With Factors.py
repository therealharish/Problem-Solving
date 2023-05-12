class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        factors = {}
        for i in range(len(arr)):
            factors[arr[i]] = []
            for j in range(i-1, -1, -1):
                num = arr[i]//arr[j]
                if arr[i]%arr[j]==0 and num in factors:
                    factors[arr[i]].append((arr[j], num))

        print(factors)
        
        res = {}
        def solve(n):
            if n in res:
                return res[n]
            ans = 0
            for (a, b) in factors[n]:
                if a != b:
                    ans += solve(a)*solve(b)*2
                else:
                    ans += solve(a)*solve(b)
            res[n] = ans+1
            return res[n]

        count = 0
        for i in range(len(arr)):
            count += solve(arr[i])
        return count
            
                    
                
                
            
        
        