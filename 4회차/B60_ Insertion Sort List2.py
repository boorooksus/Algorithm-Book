from typing import Optional
import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode()

        while head:
            while node.next and node.next.val < head.val:
                node = node.next

            head.next, node.next, head = node.next, head, head.next

            if head and head.val < node.val:
                node = root

        return root.next


nums = [4,2,1,3]
root = node = ListNode()
for num in nums:
    node.next = ListNode(num)
    node = node.next

head = Solution().insertionSortList(root.next)
while head:
    print(head.val, end=' ')
    head = head.next

