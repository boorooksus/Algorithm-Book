from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def cal(l1, l2, flag):
            if not l1:
                l1, l2 = l2, l1
            if not l1:
                return ListNode(1) if flag else None

            if l2:
                l1.val += l2.val
            l1.val += flag
            if l1.val >= 10:
                l1.val %= 10
                flag = 1
            else:
                flag = 0

            if l2:
                l1.next = cal(l1.next, l2.next, flag)
            else:
                l1.next = cal(l1.next, None, flag)
            return l1

        return cal(l1, l2, 0)


def make_list(li):
    root = node = ListNode()
    for num in li:
        node.next = ListNode(num)
        node = node.next
    return root.next


print(Solution().addTwoNumbers(make_list([2,4,9]), make_list([5,6,4,9])))
