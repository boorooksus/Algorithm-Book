from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = node = ListNode()
        root.next = head
        for _ in range(left - 1):
            node = node.next
        start = node
        for _ in range(right - left + 2):
            node = node.next
        end = node
        node = start.next
        for _ in range(right - left + 1):
            next, node.next, start.next = node.next, end, node
            end, node = node, next

        return root.next



root = ListNode()
root.next = ListNode(3)
root.next.next = ListNode(5)
print(Solution().reverseBetween(root.next, 1, 2))