from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        result = node = ListNode(None)
        carry = 0

        while l1 or l2 or carry != 0:
            x = 0
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next

            x += carry
            carry = 0
            if x > 9:
                carry = 1
                x -= 10

            node.next = ListNode(x)
            node = node.next

        return result.next
