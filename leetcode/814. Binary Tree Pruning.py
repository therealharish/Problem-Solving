# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      def postorder(root):
        # if not root:
        #   return
        # print(root)
        # if(not root.left and not root.right and root.val!=1):
        #   if rootFather:
        #     if(rootFather.left and rootFather.left.val == 0):
        #       rootFather.left = None
        #     elif(rootFather.right and rootFather.right.val == 0):
        #       rootFather.right = None
        #     return
        if not root:
          return None
        left = postorder(root.left)
        right = postorder(root.right)
        if(left == None):
          root.left = None
        if(right == None):
          root.right = None
        if(not left and not right and root.val == 0):
          root = None
        return root
        

      if (root):
            postorder(root)
            if (root.val == 0 and not root.left and not root.right):
                return None
            else:
                return root
      else:
            return None