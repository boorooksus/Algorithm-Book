from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        root.next = head

        while head and head.next:
            head.next, prev.next, prev.next.next = head.next.next, head.next, head
            head, prev = head.next, prev.next.next

        return root.next


x = [1,2,3,4]
root = node = ListNode(None)
for i in x:
    node.next = ListNode(i)
    node = node.next

Solution().swapPairs(root.next)
