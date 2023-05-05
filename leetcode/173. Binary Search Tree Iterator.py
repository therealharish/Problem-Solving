# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
      self.l=[]
      def inorder(root):
        if not root:
          return None
        else:
          inorder(root.left)
          self.l.append(root.val)
          inorder(root.right)
      inorder(root)

    def next(self) -> int:
        return self.l.pop(0)

    def hasNext(self) -> bool:
        if len(self.l)!=0:
          return True
        else:
          return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()