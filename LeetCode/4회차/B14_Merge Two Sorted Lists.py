from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = node = ListNode(None)

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                node, list1 = node.next, list1.next
            else:
                node.next = list2
                node, list2 = node.next, list2.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return root.next

