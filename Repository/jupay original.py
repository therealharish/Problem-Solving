class Node:
    def __init__(self, v, parent):
        self.v = v
        self.links = []
        self.parent = parent
        self.anc_locked = 0
        self.dec_locked = 0
        self.uid = 0
        self.isLocked = False

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
        r.addLinks(temp, r)
        st += m
        q.extend(r.links)
    return root


class Tree:
    def __init__(self, r):
        self.root = r
        self.vton = {}

    def getRoot(self):
        return self.root

    def fillVtoN(self, r):
        if not r:
            return
        self.vton[r.v] = r
        for k in r.links:
            self.fillVtoN(k)

    def informDecendants(self, r, val):
        for k in r.links:
            k.anc_locked += val
            self.informDecendants(k, val)

    def verifyDecendants(self, r, id, v):
        if r.isLocked:
            if r.uid != id:
                return False
            v.append(r)
        if r.dec_locked == 0:
            return True
        ans = True
        for k in r.links:
            ans &= self.verifyDecendants(k, id, v)
            if not ans:
                return False
        return ans

    def lock(self, v, id):
        t = self.vton[v]
        if t.isLocked:
            return False
        if t.anc_locked != 0:
            return False
        if t.dec_locked != 0:
            return False
        cur = t.parent
        while cur:
            cur.dec_locked += 1
            cur = cur.parent
        self.informDecendants(t, 1)
        t.isLocked = True
        t.uid = id
        return True

    def unlock(self, v, id):
        t = self.vton[v]
        if not t.isLocked:
            return False
        if t.isLocked and t.uid != id:
            return False
        cur = t.parent
        while cur:
            cur.dec_locked -= 1
            cur = cur.parent
        self.informDecendants(t, -1)
        t.isLocked = False
        return True

    def upgrade(self, v, id):
        t = self.vton[v]
        if t.isLocked:
            return False
        if t.anc_locked != 0:
            return False
        if t.dec_locked == 0:
            return False
        vec = []
        if self.verifyDecendants(t, id, vec):
            for k in vec:
                self.unlock(k.v, id)
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

r = Node(s[0], None)
r = buildTree(r, m, s)

t = Tree(r)
t.fillVtoN(t.getRoot())

for _ in range(q):
    op, sq, uid = map(str, input().split())
    uid = int(uid)
    if op == "1":
        if t.lock(sq, uid):
            print("true")
        else:
            print("false")
    elif op == "2":
        if t.unlock(sq, uid):
            print("true")
        else:
            print("false")
    elif op == "3":
        if t.upgrade(sq, uid):
            print("true")
        else:
            print("false")