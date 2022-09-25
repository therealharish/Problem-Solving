# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = ListNode()
        head = add
        carry = 0
        while(l1 or l2):
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            add.val = l1.val + l2.val + carry
            if(add.val>9):
                add.val-=10
                carry=1
            else:
                carry=0
            l1 = l1.next
            l2 = l2.next
            add.next = ListNode()
            add = add.next
        add.val+=carry
        temp = head
        y = None
        if(add.val!=1):
            while(head.next!=None):
                y = head
                head = head.next
            y.next = None
        return temp
            
            
                
            
            
            