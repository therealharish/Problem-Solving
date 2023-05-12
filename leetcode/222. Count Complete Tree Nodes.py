# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def findLeftHeight(root):
            if not root:
                return 0
            return 1+findLeftHeight(root.left)
        
        def findRightHeight(root):
            if not root:
                return 0
            return 1+findRightHeight(root.right)
        
        def solve(root):
            if not root:
                return 0
            leftHeight = findLeftHeight(root)
            rightHeight = findRightHeight(root)
            if leftHeight == rightHeight:
                return 2**leftHeight-1
            else:
                return 1 + solve(root.left) + solve(root.right)
            
        return solve(root)