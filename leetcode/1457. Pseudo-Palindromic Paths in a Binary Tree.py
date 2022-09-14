# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = []
        digits = {1:0,
                 2:0,
                 3:0,
                 4:0,
                 5:0,
                 6:0,
                 7:0,
                 8:0,
                 9:0
                 }
        
        def dfs(root, digits, res):
            if not root:
                return
            digits[root.val]+=1
            if(root.left == None and root.right == None):
                count = 0
                print(digits)
                for x,y in digits.items():
                    if(y&1):
                        count+=1
                if(count<2):
                    res.append(1)
            else:
                dfs(root.left, digits, res)
                dfs(root.right, digits, res)
            digits[root.val]-=1
        
        dfs(root, digits, res)
        return sum(res)
        
        