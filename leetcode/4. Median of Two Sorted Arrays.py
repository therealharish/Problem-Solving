# Method 1 in notes 1 pg 21
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l = []
#         i=0
#         j=0
#         while(i<len(nums1) and j<len(nums2)):
#             if(nums1[i]<=nums2[j]):
#                 l.append(nums1[i])
#                 i+=1
#             elif(nums1[i]>nums2[j]):
#                 l.append(nums2[j])
#                 j+=1
#         while(i<len(nums1)):
#             l.append(nums1[i])
#             i+=1
#         while(j<len(nums2)):
#             l.append(nums2[j])
#             j+=1
#         n = len(nums1)+len(nums2)
#         if(n&1):
#             return l[n//2]
#         else:
#             ans = (l[n//2-1]+l[(n//2)])/2
#             return ans



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# # Method 2 in notes 1 pg 21
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l = []
#         i=0
#         j=0
#         k=(len(nums1)+len(nums2))//2
        
#         while(i<len(nums1) and j<len(nums2) and len(l)<=k):
#             if(nums1[i]<=nums2[j]):
#                 l.append(nums1[i])
#                 i+=1
#             elif(nums1[i]>nums2[j]):
#                 l.append(nums2[j])
#                 j+=1
#         while(i<len(nums1) and len(l)<=k):
#             l.append(nums1[i])
#             i+=1
#         while(j<len(nums2) and len(l)<=k):
#             l.append(nums2[j])
#             j+=1
#         n = len(nums1)+len(nums2)
#         if(n&1):
#             return l[k]
#         else:
#             ans = (l[k-1]+l[k])/2
#             return ans

# ==============================================================================


# Method 3 in notes 1 pg 21
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid1 = 0
        mid2 = 0
        counter = 0
        i=0
        j=0
        k=(len(nums1)+len(nums2))//2
        
        while(i<len(nums1) and j<len(nums2) and counter<=k):
            if(nums1[i]<=nums2[j]):
                counter+=1
                if(counter == k-1):
                  mid1 = nums1[i]
                if(counter == k)
                  mid2 = nums1[i]
                i+=1
            elif(nums1[i]>nums2[j]):

                counter+=1
                if(counter == k-1):
                  mid1 = nums2[j]
                if(counter == k)
                  mid2 = nums2[j]
                j+=1
              
        while(i<len(nums1) and counter<=k):
            counter+=1
            if(counter == k-1):
                mid1 = nums1[i]
            if(counter == k)
              mid2 = nums1[i]
            i+=1
          
        while(j<len(nums2) and len(l)<=k):
            counter+=1
            if(counter == k-1):
                mid1 = nums2[j]
              if(counter == k)
                mid2 = nums2[j]
            j+=1
        n = len(nums1)+len(nums2)
        if(n&1):
            return mid2
        else:
            ans = (mid1+mid2)/2
            return ans