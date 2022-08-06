from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node, prev, head, cnt: int) -> Optional[ListNode]:
            if cnt == 0:
                head.next = node
                return prev
            next, node.next = node.next, prev
            return reverse(next, node, head, cnt - 1)

        root = node = ListNode()
        root.next = head
        for _ in range(left - 1):
            node = node.next
        node.next = reverse(node.next, None, node.next, right - left + 1)
        return root.next


root = ListNode()
root.next = ListNode(3)
root.next.next = ListNode(5)
print(Solution().reverseBetween(root.next, 1, 2))