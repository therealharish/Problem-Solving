# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dum=ListNode()
      while(list1.next and list2.next):
        if(list1.val<list2.val):
          dum.val = list1.val
          dum.next = None
          list1=list1.next
        