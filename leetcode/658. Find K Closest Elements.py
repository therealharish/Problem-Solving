class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr)-1
        best = -1
        bestDiff = float('inf')
        while(low <= high):
            mid = (low+high)//2
            if(abs(arr[mid]-x)<bestDiff):  
                best = mid
                bestDiff = abs(arr[mid]-x)
            elif(abs(arr[mid]-x)==bestDiff):
                best = min(best, mid)
            if(arr[mid] == x):
                best = mid
                break
            elif(arr[mid]>x):
                high = mid-1
            else:
                low = mid+1
        print(best)
        
        ans = [arr[best]]
        left = best-1
        right = best+1
        
        while(len(ans)<k):
            
            n = len(arr)
            
            
            if(left>=0 and right < n and (x-arr[left])<(arr[right]-x)):
                ans.append(arr[left])
                left-=1
            elif(left>=0 and right<n and len(ans)<k and (x-arr[left])>(arr[right]-x)):
                ans.append(arr[right])
                right+=1
            elif(left>=0):
                ans.append(arr[left])
                left-=1
            elif(right<n and len(ans)<k):
                ans.append(arr[right])
                right+=1
                
        return sorted(ans)
            
            