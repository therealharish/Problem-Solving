# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        first = head
        second = head
        
        for i in range(n):
            second = second.next
        
        while(second):
            if not prev:
                prev = head
            else:
                prev = prev.next
            first = first.next
            second = second.next
            
        if not prev:
            head = head.next
        else:
            prev.next = first.next
            
#         if not first:
#             prev = None
#         else:
#             prev.next = first.next
            
        return head
    
    
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        first = head
        second = head
        
        for i in range(n):
            second = second.next
            
        while(second):
            if not prev:
                prev = head
            else:
                prev = prev.next
            first = first.next
            second = second.next
            
        if not prev:
            head = head.next
        else:
            prev.next = first.next
            
        return head
        