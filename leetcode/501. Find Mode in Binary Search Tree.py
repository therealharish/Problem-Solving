# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        
        def inorder(root):
            if not root:
                return
            else:
                inorder(root.left)
                if(root.val not in d):
                    d[root.val]=1
                else:
                    d[root.val]+=1
                inorder(root.right)
        inorder(root)
        m = max(list(d.values()))
        l=[]
        for x,y in d.items():
            if(y==m):
                l.append(x)
        return l