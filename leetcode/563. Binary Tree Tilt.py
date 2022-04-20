# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

      def sumTree(root, s):
        if not root:
          return None
        else:
          sumTree(root.left, s)
          s+=root.val
          sumTree(root.right, s)
        return s
      def makeTilt(root):
        if not root:
          return None
        else:
            makeTilt(root.left)
            if(root.left == None and root.right==None):
                root.val=0
            elif(root.right==None):
                root.val = root.right.val
            elif(root.left==None):
                root.val=root.left.val
            else: root.val = abs(sumTree(root.left, 0)-sumTree(root.right, 0))
            makeTilt(root.right)
        return root

      tilted = makeTilt(root)
      def findsumTilt(root, sum):
        if not root:
          return None
        else:
          findsumTilt(root.left, sum)
          sum+=root.val
          findsumTilt(root.right, sum)
        return sum
      sum =  findsumTilt(tilted, 0)
      return sum
            
            
        