# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeightLeft(root):
            if not root:
                return 0

            return getHeightLeft(root.left) + 1
		
        def getHeightRight(root):
            if not root:
                return 0

            return getHeightRight(root.right) + 1
        
        def traverse(root):
            if not root:
                return 0
            left = getHeightLeft(root)
            right = getHeightRight(root)
            print(left, right)
            if(left == right):
                return 2**left - 1
            else:
                return 1 + traverse(root.left) + traverse(root.right)


        return traverse(root)
