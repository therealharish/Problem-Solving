# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if(not head):
            return None
        l1 = None
        l2 = None
        t1 = None
        t2 = None
        temp = head
        while(temp!=None):
            if(temp.val < x):
                if(not l1):
                    l1 = temp
                    t1 = l1
                else:
                    t1.next = temp
                    t1 = t1.next
            else:
                if(not l2):
                    l2 = temp
                    t2 = l2
                else:
                    t2.next = temp
                    t2 = t2.next
            temp = temp.next
        if(l2):
            t2.next = None
        if(l1):
            t1.next = l2
        else:
            l1 = l2
        return l1
            