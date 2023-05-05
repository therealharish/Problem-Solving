# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





# class Solution:
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#       s=defaultdict(float)
#       t=defaultdict(int)
    

#       def dfs(root, level):
#         if not root:
#           return None
#         s[level]+=root.val
#         t[level]+=1
#         dfs(root.left, level+1)
#         dfs(root.right, level+1)

#       l=[]
#       dfs(root, 0)
#       for x,y in s.items():
#         l.append(s[x]/t[x])
#         print(s[x], t[x])

#       return l




# 2,9,2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum = defaultdict(float)
        num = defaultdict(int)
        def preorder(node, level):
            if not node:
                return
            else:
                sum[level]+=node.val
                num[level]+=1
                preorder(node.left, level+1)
                preorder(node.right, level+1)
        
        preorder(root, 0)
        l = []
        for i in sum:
            l.append(sum[i]/num[i])
        return l
        
      