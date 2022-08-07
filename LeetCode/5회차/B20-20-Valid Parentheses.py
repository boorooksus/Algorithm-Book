class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in table:
                stack.append(char)
            else:
                if not stack or char != table[stack.pop()]:
                    return False

        return len(stack) == 0


print(Solution().isValid("()[]{}"))
