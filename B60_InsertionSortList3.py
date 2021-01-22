# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        parent = cur = ListNode(None)

        while head:
            while cur.next and head.val > cur.next.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            cur = parent

        return parent.next

"""
leetcode: 147
링크드리스트 Insertion Sort 구현.
"""