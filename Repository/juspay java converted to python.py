class Node:
    def __init__(self):
        self.isLocked = False
        self.id = 0
        self.parent = None
        self.anc_locked = 0
        self.des_locked = 0
        self.child = []

def change(node, val):
    if node is None:
        return
    node.anc_locked += val
    for i in node.child:
        change(i, val)

def lock(node, id):
    if node.isLocked:
        return False
    if node.anc_locked > 0 or node.des_locked > 0:
        return False
    parent = node
    while parent is not None:
        parent.des_locked += 1
        parent = parent.parent
    change(node, 1)
    node.isLocked = True
    node.id = id
    return True

def unlock(node, id):
    if not node.isLocked or node.id!= id:
        return False
    parent = node
    while parent is not None:
        parent.des_locked -= 1
        parent = parent.parent
    change(node, -1)
    node.isLocked = False
    node.id = 0
    return True

def getAllChilds(node, a, id):
    if node is None:
        return True
    if node.isLocked:
        if id!= node.id:
            return False
        else:
            a.append(node)
    if node.des_locked == 0:
        return True
    for i in node.child:
        ans = getAllChilds(i, a, id)
        if not ans:
            return False
    return True

def upgrade(node, id):
    if node.isLocked or node.anc_locked > 0 or node.des_locked == 0:
        return False
    a = []
    can = getAllChilds(node, a, id)
    if not can:
        return False
    change(node, 1)
    for i in a:
        unlock(i, id)
    node.isLocked = True
    node.id = id
    return True

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = input().split()
    root = Node()
    hash = {arr[0]: root}
    que = [root]
    index = 1
    while que and index < n:
        size = len(que)
        for i in range(size):
            rem = que.pop(0)
            for j in range(1, k+1):
                if index >= n:
                    break
                newNode = Node()
                newNode.parent = rem
                hash[arr[index]] = newNode
                rem.child.append(newNode)
                que.append(newNode)
                index += 1
    q = int(input())
    for i in range(q):
        val, str, id = map(int, input().split())
        node = hash[str]
        if val == 1:
            ans = lock(node, id)
        elif val == 2:
            ans = unlock(node, id)
        else:
            ans = upgrade(node, id)
        print(ans)