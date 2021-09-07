from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = head = ListNode(None)

        while True:
            is_done = True
            for i in lists:
                if i:
                    is_done = False
                    break
            if is_done:
                break

            # min_node = ListNode(None)
            # min_node.next = lists[0]
            # for i in lists[1:]:
            #     if i is not None and i.val < min_node.next.val:
            #         min_node.next = i
            # head.next = min_node.next
            # min_node.next = min_node.next.next
            # head = head.next
            min_node = ListNode(100000)
            min_idx = -1
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_idx = i
            head.next = min_node
            lists[min_idx] = lists[min_idx].next
            head = head.next


        return root.next


# leetcode: 23
# 시간 초과
