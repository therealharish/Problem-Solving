# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def solve(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            res = []
            for root in range(left, right + 1):
                lefts = solve(left, root - 1)
                rights = solve(root + 1, right)
                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(root, l, r))
            return res
        
        return solve(1, n)
                
            