# code in copy, page 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#   def levelOrder(self, root: 'Node') -> List[List[int]]:
#     res = []
#     def fun(root):
#         if(root == None):
#             return
#         for child in root.children:
#             fun(child)
#             res.append(child.val)
#     if(root==None):
#         res = []
#     else:
#       res.append(root.val)
#       fun(root)
#       return res
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [root, None]
        res = []
        l = []
        while (queue):
            ele = queue.pop(0)
            if (ele == None and l == []):
                res.append(l)
                l = []
                queue.append(None)
            else:
                l.append(ele.val)
                for i in ele.children:
                    queue.append(i)
        return res
