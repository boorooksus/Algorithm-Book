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

        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        left, right, slow.next = head, slow.next, None
        left = self.sortList(left)
        right = self.sortList(right)

        result = node = ListNode(None)
        while left and right:
            if left.val < right.val:
                node.next = left
                node, left = node.next, left.next
            else:
                node.next = right
                node, right = node.next, right.next

        if left:
            node.next = left
        elif right:
            node.next = right

        return result.next


