# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        left = mid = right = ListNode(0)
        left.next = head
        while right.next and right.next.next:
            mid, right = mid.next, right.next.next

        b = self.sortList(mid.next)
        mid.next = None
        a = self.sortList(left.next)

        cur = root = ListNode(0)
        while a and b:
            if a.val < b.val:
                cur.next = a
                a, cur = a.next, cur.next
            else:
                cur.next = b
                b, cur = b.next, cur.next

        if a:
            cur.next = a
        if b:
            cur.next = b

        return root.next

"""
4 2  1 3
4   2  1   3

"""