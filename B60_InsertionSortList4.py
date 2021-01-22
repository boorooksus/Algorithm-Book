# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        parent = cur = ListNode(None)

        while head:
            while cur.next and head.val > cur.next.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.next.val > head.val:
                cur = parent

        return parent.next

"""
leetcode: 147
링크드리스트 Insertion Sort 구현.
이전 버전 속도 개선.
cur의 값이 head보다 큰 경우만 parent로 되돌아가도록 함.
"""