class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):
        def search(arr, target):
            low = 0
            high = len(arr)-1
            ans = 0
            while(low<=high):
                mid = (low+high)//2
                if(arr[mid]<target):
                    ans = mid+1
                    low = mid+1
                else:
                    high = mid-1
            return ans
        
        
        low = 1
        high = 10**12
        ans = 0
        size = len(A)*len(A[0])
        req = size//2
        while(low<=high):
            mid = (low+high)//2
            count = 0
            for i in range(len(A)):
                count+=search(A[i], mid)
            # print(count, 2)
            # if (count == req):
            #     return mid
            if(count <= req):
                ans = mid
                low = mid+1
                # this is because there could be duplicate elements like [1,2,2,2,3,7]
            else:
                high = mid-1
        return ans
            
                
    