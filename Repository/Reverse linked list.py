# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      prev = None
      cur = head
      copy = head
      while(cur!=None):
        copy = cur
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        copy = copy.next
      print(prev)
      print(copy)
      cur = head
      while cur:
        print(cur)
        i = cur
        j = prev
        print(i.val, j.val)
        if(i.val != j.val):
          return False
        cur = cur.next
        prev = prev.next
      return True
          
        
    
      