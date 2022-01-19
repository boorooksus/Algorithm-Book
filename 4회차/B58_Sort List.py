from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = fast = head
        prev = ListNode()
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        root = node = ListNode()

        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next

            node = node.next

        node.next = left or right

        return root.next

