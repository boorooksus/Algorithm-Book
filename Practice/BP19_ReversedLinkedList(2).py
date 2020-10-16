# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = head
        prev = ListNode(None)
        prev.next = head
        i = 1
        while i < m:
            head, prev = head.next, prev.next
            i += 1
        temp = ListNode(None)
        while i <= n:
            next, temp.next = temp.next, head
            head, temp.next.next = head.next, next
            i += 1
        prev.next = temp.next
        while temp.next:
            temp = temp.next
        temp.next = head
        return root


sol = Solution()
root = head = ListNode(None)

head.next = ListNode(3)
head = head.next
head.next = ListNode(5)

sol.reverseBetween(root.next, 1, 2)

# 채점 결과: Wrong Answer
