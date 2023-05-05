class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        
        if(len(A)<B):
            return -1
        
        def check(A, bar, B):
            s = 0
            count = 1
            
            for i in range(len(A)):
                if(bar<A[i]):
                    return float('inf')
                
                if(s+A[i]<=bar):
                    s+=A[i]
                else:
                    count+=1
                    s=A[i]
                    
            return count
                
        
        low = min(A)
        high = sum(A)
        # print(low, high)
        best = 0
        while(low<=high):
            mid = (low+high)//2
            # print(best, mid)
            if(check(A, mid, B) <= B):
                best = mid
                high = mid-1
            else:
                low = mid+1
        return best

    