# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def check(l1, l2):
            if len(l1)!=len(l2):
                return False
            for i in range(len(l1)):
                if(l1[i]!=l2[i]):
                    return False
        
            return True

        def pre(root, l):
            if not root:
                return root
            if not root.left and not root.right:
                l.append(root.val)
                return 
            pre(root.left, l)
            pre(root.right, l)
        l1 = []
        l2 = []
        pre(root1, l1)
        pre(root2, l2)
        # print(l1, l2)
        if(check(l1, l2)):
            return True
        return False

