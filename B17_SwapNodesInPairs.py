# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        left = ListNode(head.val)
        node = head.next
        next, node.next = node.next, left
        node.next.next = self.swapPairs(next)

        return node

