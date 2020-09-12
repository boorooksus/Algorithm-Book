from typing import List
from collections import deque

class Solution:
    def reverseString(self, s: List[str]) -> None:
        dq = deque()
        while s:
            dq.append(s.pop())
        while dq:
            s.append(dq.popleft())

