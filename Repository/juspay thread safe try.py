# '''
# # Sample code to perform I/O:

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

# # Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
# '''

# # Write your code here


from collections import deque
class Node:
    def __init__(self, v, parent):
        self.vertex = v
        self.id = 0
        self.links = []
        self.parent = parent
        # self.anLocked = 0
        self.deLocked = 0
        self.isLocked = False
        self.reading = 0
        self.writing = 0

    def addLinks(self, l, p):
        for i in l:
            self.links.append(Node(i, p))

def buildTree(root, m, nodeNames):
    q = deque()
    q.append(root)
    st = 1
    while(q):
        node = q.popleft()
        if st >= len(nodeNames):
            continue
        temp = nodeNames[st: st + m]
        node.addLinks(temp, node)
        st += m
        q.extend(node.links)
    return root

class Tree:
    def __init__(self, node):
        self.root = node
        self.dict = {}


    def getRoot(self):
        return self.root

    def filldict(self, node):
        if not node:
            return 
        self.dict[node.vertex] = node
        for k in node.links:
            self.filldict(k)
            
    def checkAncestors(self, node):
      curr = node.parent
      while (curr):
        if curr.writing:
          return False
        if curr.isLocked:
            return False
        curr = curr.parent
      return True
      
        
    
#     def increment(self, node):
#         for i in node.links:
#             i.anLocked += 1
#             self.increment(i)

#     def decrement(self, node):
#         for i in node.links:
#             i.anLocked -= 1
#             self.decrement(i)

    def verifyDecendants(self, node, arr, id):
        if node.isLocked:
            if node.id != id:
                return False
            arr.append(node)
        if node.deLocked == 0:
            return True
        ans = True
        for j in node.links:
            ans &= self.verifyDecendants(j, arr, id)
            if not ans:
                return False
        return ans


    # def lockNotThreadSafe(self, v, id):
    #     t = self.dict[v]
    #     if t.isLocked:
    #         return False
    #     # if t.anLocked != 0:
    #     #     return False
    #     if t.deLocked != 0:
    #         return False
    #     curr = t.parent
    # while (curr):
    # 				if curr.isLocked:
    #     				return False
    #       	curr = curr.parent
    #     curr = t.parent
    #     while(curr):
    #         curr.deLocked += 1
    #         curr = curr.parent
    #     # self.increment(t)
    #     t.isLocked = True
    #     t.id = id
    #     return True
      
		# thread safe lock
    def lock(self, v, id):
        t = self.dict[v]
        
        if t.writing:
          return False
      
        t.writing = True
      
        if t.isLocked:
            return False
        if t.deLocked != 0:
            return False
        # if not self.checkAncestors(t):
        #   return False
      
        curr = t.parent
        changed = set()
        checked = True
        while(curr):
            if (curr.writing):
              checked = False
              break
            if curr.isLocked:
                checked = False
                break
            curr.deLocked += 1
            changed.add(curr)
            curr = curr.parent
            
        if not checked:
            for i in changed:
                i.deLocked -= 1
            return False
        # self.increment(t)
        t.isLocked = True
        t.id = id
        
        t.writing = False
        
        return True

    def unlock(self, v, id):
        t = self.dict[v]
        if not t.isLocked:
            return False
        if t.isLocked and t.id != id:
            return False
        curr = t.parent
        while curr:
            curr.deLocked -= 1
            curr = curr.parent
        # self.decrement(t)
        t.isLocked = False
        return True
    
    def upgrade(self, v, id):
        t = self.dict[v]
        if t.isLocked:
            return False
        # if t.anLocked != 0:
        #     return False
        
				# to check the ancestors
        # curr = t.parent
        # while curr:
        #   if curr.isLocked:
        #     return False
        # 	curr = curr.parent
          
        if t.deLocked == 0:
            return False
        arr = []
        if self.verifyDecendants(t, arr, id):
            for j in arr:
                self.unlock(j.vertex, id)
        else:
            return False
        self.lock(v, id)
        t.id = id
        return True

n = int(input())
m = int(input())
queries = int(input())

nodeNames = []
for i in range(n):
    nodeNames.append(input())

root = Node(nodeNames[0], None)
root = buildTree(root, m, nodeNames)

t = Tree(root) 
t.filldict(t.getRoot())

for i in range(queries):
    op, name, id = input().split()
    op = int(op)
    id = int(id)
    if op == 1:
        ans = t.lock(name, id)
    elif op == 2:
        ans = t.unlock(name, id)
    else:
        ans = t.upgrade(name, id)
    
    if ans == True:
        print('true')
    else:
        print('false')