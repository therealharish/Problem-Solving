"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        longestPath = 0
        def traverse(root, path):
            nonlocal longestPath
            if not root:
                return
            
            path.append(root)
            if not root.children:
                longestPath = max(longestPath, len(path))
            
            for child in root.children:
                traverse(child, path.copy())
            
        traverse(root, [])
        return longestPath
        