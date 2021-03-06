# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        root.next = head

        i = 0
        while head and head.next:
            if i % 2 == 1:
                head = head.next
                prev = prev.next
                i += 1
                continue
            temp = head.next
            prev.next, head.next, temp.next = head.next, temp.next, head

            prev, head = prev.next.next, head.next
            i += 2
        return root.next
