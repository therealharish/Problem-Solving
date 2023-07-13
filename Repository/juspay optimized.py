class Node:
    def __init__(self, v, parent):
        self.val = v
        self.links = []
        self.parent = parent
        # self.anLocked = 0
        self.deLocked = 0
        self.uid = 0
        self.isLocked = False
        self.lockedChild = set()

    def addLinks(self, l, p):
        for i in l:
            self.links.append(Node(i, p))

def buildTree(root, m, s):
    q = [root]
    st = 1
    while q:
        r = q.pop(0)
        if st >= len(s):
            continue
        temp = s[st:st + m]
        # print(temp)
        r.addLinks(temp, r)
        st += m
        q.extend(r.links)
    return root


class Tree:
    def __init__(self, r):
        self.root = r
        self.dict = {}

    def getRoot(self):
        return self.root
    
    def printTree(self):
        q = [self.root]
        while q:
            r = q.pop(0)
            print(r.val, r.isLocked, r.uid, r.deLocked, [i.val for i in r.lockedChild])
            q.extend(r.links)

    def fillDict(self, r):
        if not r:
            return
        self.dict[r.val] = r
        for k in r.links:
            self.fillDict(k)
            
            
    # def increment(self, r):
    #     for k in r.links:
    #         k.anLocked += 1
    #         self.increment(k)
            
    # def decrement(self, r):
    #     for k in r.links:
    #         k.anLocked -= 1
    #         self.decrement(k)

    # def verifyDecendants(self, r, id, v):
    #     if r.isLocked:
    #         if r.uid != id:
    #             return False
    #         v.append(r)
    #     if r.deLocked == 0:
    #         return True
    #     ans = True
    #     for k in r.links:
    #         ans &= self.verifyDecendants(k, id, v)
    #         if not ans:
    #             return False
    #     return ans
    
    def verifyDecendants(self, r, id, v):
        for k in v:
            if k.isLocked and k.uid != id:
                return False
        return True

    def lock(self, v, id):
        t = self.dict[v]
        if t.isLocked:
            return False
        # if t.anLocked != 0:
        #     return False
        if t.deLocked != 0:
            return False
        cur = t.parent
        while cur:
            if cur.isLocked:
                return False
            cur = cur.parent
        cur = t.parent
        while cur:
            cur.deLocked += 1
            cur.lockedChild.add(t)
            cur = cur.parent
        # self.increment(t)
        t.isLocked = True
        t.uid = id
        return True
    

    def unlock(self, v, id):
        t = self.dict[v]
        if not t.isLocked:
            return False
        if t.isLocked and t.uid != id:
            return False
        cur = t.parent
        while cur:
            cur.deLocked -= 1
            cur.lockedChild.remove(t)
            cur = cur.parent
        # self.decrement(t)
        t.isLocked = False
        return True

    def upgrade(self, v, id):
        t = self.dict[v]
        if t.isLocked:
            return False
        # if t.anLocked != 0:
        #     return False
        if t.deLocked == 0:
            return False
        # vec = []
        # if self.verifyDecendants(t, id, vec):
        #     for k in vec:
        #         self.unlock(k.val, id)
        vec = t.lockedChild.copy()
        if self.verifyDecendants(t, id, vec):
            for k in vec:
                self.unlock(k.val, id)
        else:
            return False
        self.lock(v, id)
        return True



n = int(input())

m = int(input())

q = int(input())

s = []
for _ in range(n):
    s.append(input())

root = Node(s[0], None)
root = buildTree(root, m, s)

t = Tree(root)
t.fillDict(t.getRoot())

for _ in range(q):
    op, nodeName, uid = map(str, input().split())
    uid = int(uid)
    if op == "1":
        if t.lock(nodeName, uid):
            print("true")
        else:
            print("false")
    elif op == "2":
        if t.unlock(nodeName, uid):
            print("true")
        else:
            print("false")
    elif op == "3":
        if t.upgrade(nodeName, uid):
            print("true")
        else:
            print("false")
    # t.printTree()