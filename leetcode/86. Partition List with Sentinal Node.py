# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if(not head):
            return None
        l1 = ListNode()
        l2 = ListNode()
        t1 = l1
        t2 = l2
        temp = head
        while(temp!=None):
            if(temp.val < x):
                    t1.next = temp
                    t1 = t1.next
            else:
                    t2.next = temp
                    t2 = t2.next
            temp = temp.next
        t2.next = None
        t1.next = l2.next
        
        return l1
            