class Solution1:
    def findIntegers(self, n: int) -> int:
        
        b = bin(n)[2:]
        k = len(b)
        @cache
        def count(n):
            if n == 0:
                return 1
            if n == 1:
                return 2
            return count(n-1) + count(n-2)
        
        @cache
        def solve(i):
            if i == k:
                return 1
            if i == k-1:
                if b[i] == 0:
                    return 1
                else:
                    return 2
            takeCount = count(k-1-i)
            if b[i+1]=='0':
                while(i<k-1 and b[i+1]=='0'):
                    i+=1
                return takeCount + solve(i+1)
            if b[i+1]=='1':
                return takeCount + count(k-1-i-1)
            
        return solve(0)
                
# tabulate it

                
            