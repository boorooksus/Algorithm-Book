from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    left = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def compare(right):
            if not right:
                return True

            if compare(right.next) and self.left.val == right.val:
                self.left = self.left.next
                return True

            return False

        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return compare(slow)
