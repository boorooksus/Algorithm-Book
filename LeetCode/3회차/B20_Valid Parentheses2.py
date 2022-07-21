class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or char != table[stack.pop()]:
                    return False
        return not stack


print(Solution().isValid("({{{{}}}))"))
