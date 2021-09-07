# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums = []
        while l1.next is not None:
            nums.append(l1.val)
            l1 = l1.next
        nums.append(l1.val)

        while l2.next is not None:
            nums.append(l2.val)
            l2 = l2.next
        nums.append(l2.val)

        nums.sort()
        node = ListNode()
        node.val = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            node.next = node
            node.val = nums[i]
        return node

# 오류
