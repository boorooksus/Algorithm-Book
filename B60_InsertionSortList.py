# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        node, prev = head, None
        while node and node.next:
            prev, node.prev, node = node, prev, node.next
        node.prev = prev

        node = head
        while node and node.next:
            cur = node
            while cur and cur.val > cur.next.val:
                cur.next.val, cur.val = cur.val, cur.next.val
                cur = cur.prev
            node = node.next

        return head


"""
leetcode: 147
링크드리스트 Insertion Sort 구현
"""