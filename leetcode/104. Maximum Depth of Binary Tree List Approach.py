# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = set()
        d = {}
        def preorder(root):
            
            if not root:
                return
            
            if not root.left and not root.right: 
                s.add(root)
                return
            
            if(root.left):
                if(root.left in d):
                    d[root.left].append(root)
                else:
                    d[root.left] = [root]

            if(root.right):
                if(root.right in d):
                    d[root.right].append(root)
                else:
                    d[root.right] = [root]

            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        m = 0
        for i in s:
            move = i
            count = 1
            # print(move)
            while(move in d):
                # print(move)
                count+=1
                move = d[move][0]
            m = max(m, count)
        
        # print(d)
        # print(s)
        return m