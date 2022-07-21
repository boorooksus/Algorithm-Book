class Solution:
    def isValid(self, s: str) -> bool:
        table = {']': '[', '}': '{', ')': '('}
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1] != table[char]:
                    return False
                stack.pop()

        return len(stack) == 0
    