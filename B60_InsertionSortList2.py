# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        node, prev = head, None

        node = head
        while node and node.next:
            node.prev = prev
            cur = node
            while cur and cur.val > cur.next.val:
                cur.next.val, cur.val = cur.val, cur.next.val
                cur = cur.prev
            prev, node = node, node.next

        return head


"""
leetcode: 147
링크드리스트 Insertion Sort 구현.
이전 버전에서 링크드 리스트의 prev 추가하는 작업과 탐색 과정을 합침.
(채점 결과 속도 차이 없음)
"""