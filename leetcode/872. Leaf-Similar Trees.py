# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def inorder(root, l):
            if not root:
                return None
            else:
                inorder(root.left, l)
                if(root.left==None and root.right==None):
                    l.append(root.val)
                inorder(root.right, l)
            return l
        l1=inorder(root1, [])
        l2 = inorder(root2, [])
        print(l1, l2)
        if(l1==l2):
            return True
        else:
            return False
        