# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# level order
class Solution1:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        end = False
        q = deque()
        q.append(root)
        while(q):
            node = q.popleft()
            if node is None:
                end = True
                continue
            if end and node:
                return False
            q.append(node.left)
            q.append(node.right)
        return True

# dfs
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def countNodes(root):
            if not root:
                return 0
            return 1+countNodes(root.left)+countNodes(root.right)
        
        def solve(root, i, totalNodes):
            if not root:
                return True
            if i >= totalNodes:
                return False
            return solve(root.left, 2*i+1, totalNodes) and solve(root.right, 2*i+2, totalNodes)
        
        totalNodes = countNodes(root)
        return solve(root, 0, totalNodes)