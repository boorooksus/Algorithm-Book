# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        target = head.next
        root = ListNode(None)
        root.next = head

        while target:
            next = target.next
            pre, cur = root, head

            while cur:
                if (pre.val is None and target.val < cur.val) or \
                        (pre.val < target.val < cur.val):
                    pre.next, target.next = target, cur
                    break
                pre, cur = pre.next, cur.next
            target = next

        return head
