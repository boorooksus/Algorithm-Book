from typing import Optional
import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        root.next = head

        while head and head.next:
            while head and head.next and head.val > head.next.val:
                node, target, head.next = root, head.next, head.next.next
                while node.next.val < target.val:
                    node = node.next
                target.next, node.next = node.next, target
            head = head.next

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

