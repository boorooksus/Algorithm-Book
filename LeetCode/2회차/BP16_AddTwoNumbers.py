# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)
        root.next = l1
        prev = ListNode(None)
        prev.next = l1

        save = 0
        while l2:
            l1.val += l2.val + save
            save = 0
            if l1.val >= 10:
                save += 1
                l1.val -= 10
            if l1.next is None:
                l1.next, l2.next = l2.next, None
            l1, l2, prev = l1.next, l2.next, prev.next

        while l1:
            l1.val += save
            save = 0
            if l1.val >= 10:
                save += 1
                l1.val -= 10
            l1, prev = l1.next, prev.next

        if save == 1:
            prev.next = ListNode(1)
        return root.next

# leetcode: 2
# success. 다음 버전에서 while문을 하나로 통합해 보겠음
