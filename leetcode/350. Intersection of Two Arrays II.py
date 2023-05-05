class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = Counter(nums2)
        ans = []
        for i in nums1:
            if i in d and d[i]>0:
                d[i]-=1
                ans.append(i)
        return ans
    
# two pointers approach
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        ans = []
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i]==nums2[j]):
                ans.append(nums1[i])
                i+=1
                j+=1
            elif(nums1[i]<nums2[j]):
                i+=1
            else:
                j+=1
        return ans
    