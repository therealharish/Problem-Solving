# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        # has no obligation for it's parent, it's parent is covered by something else
        dp1, dp2, dp3 = {}, {}, {}
        def f1(root):
            
            if root in dp1:
                return dp1[root]
            
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            withCamera = 1 + f2(root.left) + f2(root.right)
            
            left, right = float('inf'), float('inf')
            
            left = f3(root.left) + f1(root.right)
            right = f1(root.left) + f3(root.right)
            
            withoutCamera = min(left, right)
            dp1[root] = min(withCamera, withoutCamera)
            return dp[root]
            
        # there is no compulsion at all to put a camera here
        def f2(root):
            
            if root in dp2:
                return dp2[root]
            
            withCamera = 1 + f2(root.left) + f2(root.right)
            withoutCamera = f1(root.left) + f1(root.right)
            
            dp2[root] = min(withCamera, withoutCamera)
            return dp2[root]
        
        # compulsory to put a camera here
        def f3(root):
            
            if root in dp3:
                return dp3[root]
            
            dp3[root] = 1 + f2(root.left) + f2(root.right)
            return dp3[root]
        
        return f1(root)
            
            