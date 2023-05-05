# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = TreeNode()
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    
        if original:
            self.getTargetCopy(original.left, cloned.left, target)
            print(cloned.val)
            if(original.val == target.val):
                self.ans = cloned
            self.getTargetCopy(original.right, cloned.right, target)
        return self.ans