class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.stack = ListNode(None)

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.next = ListNode(x)
        self.stack = self.stack.next

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top = self.top()
        temp = self.root
        while temp.next == self.stack:
            temp = temp.next
        self.stack = temp
        self.stack.next = None
        # 3.5회차.next = None
        return top

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack.val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.root.next is None:
            return True
        else:
            return False


# leetcode: 225
# ListNode로 구현 실패
