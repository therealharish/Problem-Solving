# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def pushStack(self, root):
        while(root):
            self.stack.append(root)
            root = root.left
    
    def __init__(self, root: Optional[TreeNode]):      
      self.stack = []
      self.pushStack(root)

    def next(self) -> int:
      curr = self.stack.pop()
      self.pushStack(curr.right)
      return curr.val

    def hasNext(self) -> bool:
      if self.stack:
        return True
      else:
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()