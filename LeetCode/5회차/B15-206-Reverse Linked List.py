from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, node = None, head

        while node:
            res, res.next, node = node, res, node.next

        return res


x = [1,2,3,4,5]
root = cur = ListNode()
for num in x:
    cur.next = ListNode(num)
    cur = cur.next
print(Solution().reverseList(root.next))