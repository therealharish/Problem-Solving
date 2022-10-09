""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
  l=[]
  def inorder(root):
    if not root:
      return
    inorder(root.left)
    l.append(root.data)
    inorder(root.right)
  inorder(root)
  for i in range(len(l)-1):
    if(l[i]>=l[i+1]):
      return False
  return True
    
    