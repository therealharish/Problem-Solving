class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
  def paint(self, A, B, C):
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

    