class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        print(arr2)
        count=0
        for i in arr1:
            flag=0
            low= 0
            high = len(arr2)-1
            while low<=high:
                mid = (low+high)//2
                if abs(i-arr2[mid]) <= d:
                    flag=1
                    break
                elif arr2[mid]>i:
                    high = mid-1
                else:
                    low = mid+1
            if flag ==0:
                count+=1
        return count
        