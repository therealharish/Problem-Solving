# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(node1, node2):
            if(node1 is None and node2 is not None):
                return False
            elif(node1 is not None and node2 is None):
                return False
            elif(node1 is None and node2 is None):
                return True
            if(node1.val!=node2.val):
                return False
            
            return preorder(node1.left, node2.right) and preorder(node1.right, node2.left)
        
        if(preorder(root.left, root.right)):
            return True
        else:
            return False