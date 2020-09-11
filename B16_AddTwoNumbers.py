# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
            if not node:
                return prev
            node.next, next = prev, node.next
            return reverse(next, node)

        node = None
        save = 0
        while l1 and l2:
            l1.val += l2.val + save
            save = 0
            if l1.val > 9:
                save += 1
                l1.val -= 10
            l1.next, next = node, l1.next
            node, l1, l2 = l1, next, l2.next

        # l2 자릿수가 더 큰 경우
        if l2:
            l1 = l2
        
        # l1 숫자가 안남을 때까지 추가
        while l1:
            l1.val += save
            save = 0
            if l1.val > 9:
                save += 1
                l1.val -= 10
            l1.next, next = node, l1.next
            l1, node = next, l1

        # 마지막 덧셈에서 자릿수가 올라간 경우
        if save == 1:
            temp = ListNode(1)
            temp.next = node
            node = temp

        return reverse(node)


