# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True 
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        if(abs(l-r)>1):
            return False
        
        if(not self.isBalanced(root.left)):
            return False
        if(not self.isBalanced(root.right)):
            return False
        
        return True
        
    def height(self, root):
        if(not root):
            return 0
        l = self.height(root.left)+1
        r = self.height(root.right)+1
        return max(l,r)
        
        