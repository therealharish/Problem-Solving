# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], ht = 0) -> int:
        if not root:
            return 0
        ht = ht+1
        if root.left or root.right:
            x = self.maxDepth(root.left, ht)
            y = self.maxDepth(root.right, ht)
            return max(x,y)
        else:
            return ht