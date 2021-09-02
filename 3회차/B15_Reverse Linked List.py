from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        root = ListNode(None)
        root.next = head

        while head and head.next:
            temp, head.next.next, root.next,  = head.next.next, root.next, head.next
            head.next = temp

        return root.next