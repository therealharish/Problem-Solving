# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l = []
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
            
#         def minValueNode(node):
#             current = node
#             while(curret.left is not None):
#                 current = current.left
#             return current
        
        
#         def deleteNode(root, val):
#             if not root:
#                 return None

#             if(val < root.val):
#                 root.left  = deleteNode(root.left, val)
#             elif(val > root.val):
#                 root.right = deleteNode(root.right, val)
#             else:
#                 if(root.left is None):
#                     temp = root.right
#                     root = None
#                     return temp
#                 elif root.right is None:
#                     temp  = root.left
#                     root = None
#                     return temp
                
#                 temp = minValueNode(root.right)
#                 root.val = temp.val
#                 root.right = deleteNode(root.right, temp.val)
#             return root
                
        
#         if not root:
#             return None
#         else:
            
#             if(root.val < low or root.val > high):
#                 root = deleteNode(root, root.val)
#             self.trimBST(root.left, low, high)
#             self.trimBST(root.right, low, high)
#         return root

        
        def inorder(root):
            if not root:
                return None
            else:
                self.l.append(root.val)
                inorder(root.left)
                
                inorder(root.right)

        def insert(root, key):
            if root is None:
                return TreeNode(key)
            else:
                if root.val == key:
                    return root
                elif root.val < key:
                    root.right = insert(root.right, key)
                else:
                    root.left = insert(root.left, key)
            return root

        inorder(root)
        print(self.l)

        for i in self.l:
            if(i<low or i>high or i==None):
                self.l.remove(i)
        print(self.l)
        
        ans = TreeNode()
        for i in self.l:
            ans = insert(ans, i)

        return ans


         
            