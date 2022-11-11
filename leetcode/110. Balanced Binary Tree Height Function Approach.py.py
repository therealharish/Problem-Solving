class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dp = {}
        def findDepth(root):
            if not root:
                dp[root] = 0
                return dp[root]
            if(root in dp):
                return dp[root]
            l = findDepth(root.left) + 1
            r = findDepth(root.right)+1
            dp[root] = max(l,r)
            return dp[root]
        
        def check(root, dp):
            if not root:
                return True
            depthLeft = dp[root.left]
            depthRight = dp[root.right]
            if(abs(depthLeft-depthRight)>1):
                return False
            
            if(not check(root.left, dp)):
                return False
            if not check(root.right, dp):
                return False
            
            return True
        
        findDepth(root)
        return check(root, dp)