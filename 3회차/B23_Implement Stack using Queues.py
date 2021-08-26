from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.save = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q) > 1:
            self.save.append(self.q.popleft())

        result = self.q.popleft()

        while self.save:
            self.q.append(self.save.popleft())

        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q) > 1:
            self.save.append(self.q.popleft())

        result = self.q[0]
        self.save.append(self.q.popleft())

        while self.save:
            self.q.append(self.save.popleft())

        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q


x = MyStack()

x.push(1)
x.push(2)
x.pop()
x.top()