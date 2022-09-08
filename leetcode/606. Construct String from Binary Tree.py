# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root, l):
            if not root:
                return

            l.append(str(root.val))

            if (root.left == None and root.right == None):
                return

            if (root.left == None and root.right != None):
                l.append("()")
              
            if (root.left):
                l.append("(")
                preorder(root.left, l)
                l.append(")")

            if (root.right):
                l.append("(")
                preorder(root.right, l)
                l.append(")")

        l = []
        preorder(root, l)
        return "".join(l)
