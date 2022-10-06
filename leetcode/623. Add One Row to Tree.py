# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
        currDepth = 1
        if (depth == 1):
            temp = TreeNode(val)
            temp.left = root
            return temp

        def traverse(root, currDepth):
            if not root:
                return
            if (currDepth == depth - 1):
                nodeLeft = TreeNode(val)
                nodeLeft.left = root.left
                nodeRight = TreeNode(val)
                nodeRight.right = root.right
                root.left = nodeLeft
                root.right = nodeRight
                return
            traverse(root.left, currDepth + 1)
            traverse(root.right, currDepth + 1)

        traverse(root, currDepth)
        return root
