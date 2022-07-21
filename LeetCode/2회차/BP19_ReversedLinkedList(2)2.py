# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for i in range(m - 1):
            start = start.next
        end = start.next

        for i in range(n - m):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root.next


sol = Solution()
root = head = ListNode(None)

head.next = ListNode(3)
head = head.next
head.next = ListNode(5)

sol.reverseBetween(root.next, 1, 2)

# leetcode: 92
