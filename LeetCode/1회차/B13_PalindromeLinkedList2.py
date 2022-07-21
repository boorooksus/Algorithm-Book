# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        dq = deque()
        node = head
        while node is not None:
            dq.append(node.val)
            node = node.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True

# 리트코드 234
# 이전 풀이와 속도는 비슷