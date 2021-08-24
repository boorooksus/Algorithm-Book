from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()

        for cur in lists:
            node = root
            while cur:
                if not node.next:
                    node.next = cur
                    break
                elif cur.val < node.next.val:
                    node.next, cur.next, cur = cur, node.next, cur.next
                node = node.next

        return root.next


x, y, z = ListNode(1), ListNode(5), ListNode(10)
a, b, c = ListNode(2), ListNode(7), ListNode(15)
x.next, y.next = y, z
a.next, b.next = b, c
Solution().mergeKLists([x, a])
