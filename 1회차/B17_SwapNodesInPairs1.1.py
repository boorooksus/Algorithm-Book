# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node, prev = head.next, head
        node.next, next = prev, node.next

        node.next.next = self.swapPairs(next)

        return node

