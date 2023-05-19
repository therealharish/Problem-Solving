#User function Template for python3

class Solution:
    def minTime(self, root,target):
        
        parent = {}
        temp = root
        def traverse(root):
            if not root:
                return
            if root.left:
                parent[root.left] = root
                traverse(root.left)
            if root.right:
                parent[root.right] = root
                traverse(root.right)
    
        traverse(temp)
        
        def findNode(root, target):
            if not root:
                return None
            if root.data == target:
                return root
            left = findNode(root.left, target)
            if left:
                return left
            right = findNode(root.right, target)
            if right:
                return right
        
        node = findNode(root, target)
        
        def bfs(node):
            
            q = deque()
            q.append(node)
            visited = set()
            visited.add(node)
            count = 0
            while(q):
                count += 1
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr.left and curr.left not in visited:
                        q.append(curr.left)
                        visited.add(curr.left)
                    if curr.right and curr.right not in visited:
                        q.append(curr.right)
                        visited.add(curr.right)
                    if curr in parent and parent[curr] not in visited:
                        q.append(parent[curr])
                        visited.add(parent[curr])
            return count
        
        return bfs(node)
                    
                    
            
            
            
            
            
            
