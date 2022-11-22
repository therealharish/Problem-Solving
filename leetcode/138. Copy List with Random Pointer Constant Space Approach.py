"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        while(ptr):
            node = ListNode(ptr.val)
            node.next = ptr.next
            ptr.next = node
            ptr = node.next
        ptr = head
        while(ptr):
            if(ptr.random == None):
                ptr.next.random = None
            else:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        ptr = head
        ans = ListNode()
        temp = ans
        while(ptr):
            temp.next = ptr.next
            ptr = ptr.next.next
            temp = temp.next
        return ans.next