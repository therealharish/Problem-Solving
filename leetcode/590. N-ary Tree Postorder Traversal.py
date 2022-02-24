"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def fun(root):
            if(root == None):
                return
            for child in root.children:
                fun(child)
                res.append(child.val)
        if(root==None):
            res = []
        else:
            fun(root)
            res.append(root.val)
            return res
    
            
                
        