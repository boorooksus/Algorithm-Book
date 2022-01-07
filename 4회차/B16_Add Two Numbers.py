from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def cal(l1, l2, carry):
            if not l1 and not l2:
                if carry > 0:
                    return ListNode(carry)
                return l1
            if not l1 and l2:
                l1, l2 = l2, l1
            if l1 and not l2:
                node = l1
                while node and carry > 0:
                    node.val += carry
                    carry = 0
                    if node.val > 9:
                        node.val -= 10
                        carry = 1
                    if not node.next and carry > 0:
                        node.next = ListNode(0)
                    node = node.next
                return l1

            l1.val += l2.val + carry
            carry = 0

            if l1.val > 9:
                l1.val -= 10
                carry = 1

            l1.next = cal(l1.next, l2.next, carry)

            return l1

        return cal(l1, l2, 0)


