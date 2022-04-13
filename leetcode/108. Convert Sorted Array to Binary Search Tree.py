# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def arraytobst(nums, left, right):
            if left>right: return None
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = arraytobst(nums, left, mid-1)
            node.right = arraytobst(nums, mid+1, right)
            return node

        
        if(len(nums)==0):
          return null
        return arraytobst(nums, 0, len(nums)-1)

     
        
      
        
                
                    
        