class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      n1 = nums1[:m]      
      n2 = nums2[:n]
      # print(nums1, nums2)

      n1.extend(n2)
      # print(nums1)
      n1.sort()
      
      nums1 = n1
      print(id(n1))
      print(id(nums1))
      
    
        
 # class Solution:
 #     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
 #         nums1.extend(nums2)
 #         nums1.sort()
 #         for i in range(len(nums1)):
 #                if nums1[i]==0:
 #                    nums1.remove(0)
      
