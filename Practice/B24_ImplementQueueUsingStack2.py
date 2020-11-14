class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        for i in range(len(self.output)):
            self.input.append(self.output.pop())
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        # == 1 =========================
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # == 1 ===============================
        for i in range(len(self.input)):
            self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.input == self.output == []:
            return True
        else:
            return False


# 내 풀이
# peek에서 input에 원소 하나 남기고 그거 pop 하는 방식 썼다가
# 계속 틀림(pop을 연속으로 사용하면 input에 원소가 없는데
# pop하기 때문
