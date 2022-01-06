from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        nums = deque([])

        while node:
            nums.append(node.val)
            node = node.next

        while len(nums) > 1:
            left, right = nums.popleft(), nums.pop()
            if left != right:
                return False

        return True
    