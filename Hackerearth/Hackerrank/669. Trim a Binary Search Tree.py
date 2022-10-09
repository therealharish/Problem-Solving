# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
      if not root:
          return None
      else:
          self.trimBST(root, low, high)
          
          if(root.val < low or root.val > high):
            leftchild = root.left
            rightchild = root.right
            
            
                
