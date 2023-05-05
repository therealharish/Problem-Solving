# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        pointer = ans
        while(l1 and l2):
            digit = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            digit = (l1.val+carry)%10
            carry = (l1.val+carry)//10
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l1 = l1.next
        while(l2):
            digit = (l2.val+carry)%10
            carry = (l2.val+carry)//10
            pointer.next = ListNode(digit)
            pointer = pointer.next
            l2 = l2.next
        if carry:
            pointer.next = ListNode(carry)
            pointer = pointer.next
        return ans.next