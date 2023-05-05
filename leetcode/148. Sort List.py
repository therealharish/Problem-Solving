# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      def getMid(self, head):
        slow, fast = head, head.next;
        while(fast!=None and fast.next!=None):
          slow = slow.next
          fast = fast.next.next;
        return slow

      
      def merge(self, left, right):
        
        



      
      if (head==None or head.next==None):
        return head

      left = head
      right = self.getMid(head)
      right = right.next
        