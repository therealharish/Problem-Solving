# DP APPROACH

# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:

#       dp = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]
      

#       for i in range(1, len(nums1)+1):
#         for j in range(1, len(nums2)+1):
#           if(nums1[i-1]==nums2[j-1]):
#             dp[i][j]=dp[i-1][j-1]+1

#       m = -10**9
#       for i in dp:
#         m = max(m, max(i))
#       return m

# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------

# Sliding Window APPROACH

# DP APPROACH

# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:

#       dp = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]
      

#       for i in range(1, len(nums1)+1):
#         for j in range(1, len(nums2)+1):
#           if(nums1[i-1]==nums2[j-1]):
#             dp[i][j]=dp[i-1][j-1]+1

#       m = -10**9
#       for i in dp:
#         m = max(m, max(i))
#       return m

# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------

# Sliding Window APPROACH

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

      def search(l):
        count = 0
        for i in range(len(nums1)-len(l)+1):
            if(nums1[i]==l[0]):
                if(nums1[i:i+len(l)] == l):
                    return True
        return False

      sub = []
      m =0
      for k in range(len(nums2)):
        sub.append(nums2[k])
        if(search(sub)):
          m = max(m, len(sub))
        else:
          sub = sub[1:]
      return  m