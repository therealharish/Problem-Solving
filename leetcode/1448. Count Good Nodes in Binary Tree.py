# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

      def preorder(node, maxVal):
        if not node:
          return 0
          
        if(node.val>=maxVal):
          res = 1
        else:
          res = 0

        maxVal = max(maxVal, node.val)

        res+= preorder(node.left, maxVal)
        res+= preorder(node.right, maxVal)

        return res

      return preorder(root, root.val)
        
          