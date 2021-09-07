# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def get_len(head: ListNode) -> int:
            if not head:
                return 0

            cur, idx = head, 1
            while cur and cur.next:
                idx += 1
                cur = cur.next
            return idx

        node = head
        end = get_len(head)

        for i in range(end):
            for j in range(1, end - i + 1):
                if node and node.next and node.val > node.next.val:
                    node.val, node.next.val = node.next.val, node.val
                node = node.next
            node = head

        return head


"""
leetcode: 148
버블정렬. 시간 초과
"""