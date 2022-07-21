# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even_root = even = ListNode(None)
        prev = ListNode(None)
        prev.next = head
        root = head

        while head and head.next:
            even.next = head.next
            head.next, prev.next = head.next.next, head
            head, even, prev = head.next, even.next, prev.next
        if prev.next and even_root.next:
            even.next = None
            head.next = even_root.next
        elif prev.next is None and even_root.next:
            even.next = None
            prev.next = even_root.next
        return root





sol = Solution()
root = head = ListNode(None)
for i in range(1, 6):
    head.next = ListNode(i)
    head = head.next
sol.oddEvenList(root.next)

# leetcode: 328
# 다음엔 while문의 기준을 head가 아닌 even으로 잡도록 하자
