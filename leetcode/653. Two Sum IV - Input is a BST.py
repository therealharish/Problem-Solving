# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def preorder(root, s):
            if not root:
                return False
            if (root.val in s):
                return True
            else:
                s.add(k - root.val)

            return preorder(root.left, s) or preorder(root.right, s)

        return preorder(root, set())
