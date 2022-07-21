from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode(None)
        carry = 0

        while l1 or l2 or carry > 0:
            res = carry

            if l1:
                res += l1.val
                l1 = l1.next

            if l2:
                res += l2.val
                l2 = l2.next

            carry, res = divmod(res, 10)
            node.next = ListNode(res)
            node = node.next

        return root.next
