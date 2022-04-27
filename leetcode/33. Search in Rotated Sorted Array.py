class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(nums, l, r, target):
            if(l<=r):
                mid=(l+r)//2
                print(mid)
                if(nums[mid]==target):
                    return mid
                elif(nums[mid]<target):
                    return binary(nums, mid+1, r, target)
                elif(nums[mid]>target):
                    return binary(nums, l, mid-1, target)
            return -1
        
        
        l=0
        h = len(nums)-1
        piv=-1
        while(l<=h):
            mid = (l+h)//2
            if(nums[0]<=nums[mid]):
                l = mid+1
            elif(nums[0]>=nums[mid]):
                h = mid-1
                piv = mid
                
        print(piv)
        
        if(piv==-1):
            return binary(nums, 0, len(nums)-1, target)
        elif(target == nums[piv]):
            return piv
        elif(nums[0]<=target):
            return binary(nums, 0, piv-1, target)
        else:
            return binary(nums, piv, len(nums)-1, target)

        
            
            