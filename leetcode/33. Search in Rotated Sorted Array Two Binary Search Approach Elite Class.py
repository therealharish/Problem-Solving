class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr)-1
        
        def findRotation(l, r):
            if(arr[l]<arr[r]):
                return 0
            if(len(arr)==1):
                return 0
            else:
                while(l<=r):
                    mid = (l+r)//2
                    if(arr[mid]>arr[mid+1]):
                        return mid+1
                    elif(arr[mid]>=arr[l]):
                        l = mid+1
                    else:
                        r = mid-1
        
        def binarySearch(start, end, target):
            while(start<=end):
                mid = (start+end)//2
                if(target == arr[mid]):
                    return mid
                elif(target > arr[mid]):
                    start = mid+1
                else:
                    end = mid-1
            return -1
        
        rotatedPos = findRotation(l, r)
        print(rotatedPos)
        if(arr[rotatedPos] == target):
            return rotatedPos
        if(rotatedPos == 0):
            return binarySearch(0, len(arr)-1, target)
        elif(target >= arr[0]):
            return binarySearch(0, rotatedPos-1, target)
        else:
            return binarySearch(rotatedPos, len(arr)-1, target)
        
    
    
        