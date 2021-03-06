# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = prev = ListNode(None)
        root.next = l1
        save = 0

        while l1:
            if l2:
                l1.val += l2.val
            l1.val += save
            save = 0
            if l1.val >= 10:
                save += 1
                l1.val -= 10
            if l2 and l1.next is None:
                l1.next, l2.next = l2.next, l1.next
            l1, prev = l1.next, prev.next
            if l2:
                l2 = l2.next

        if save == 1:
            prev.next = ListNode(1)
        return root.next

# leetcode: 2
#
