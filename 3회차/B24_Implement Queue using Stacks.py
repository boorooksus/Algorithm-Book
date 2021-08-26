class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.save = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.q:
            return -1
        while self.q:
            self.save.append(self.q.pop())

        result = self.save.pop()

        while self.save:
            self.q.append(self.save.pop())

        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.q:
            return -1
        while self.q:
            self.save.append(self.q.pop())

        result = self.save[-1]

        while self.save:
            self.q.append(self.save.pop())

        return result

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.q) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()