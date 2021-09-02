from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        left, right = head, head.next

        while right and right.next:
            temp, temp2, left.next = right.next.next, left.next, right.next
            right.next.next, right.next = temp2, temp
            left, right = left.next, right.next

        return head


