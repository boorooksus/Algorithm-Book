class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or abs(ord(char) - ord(stack.pop())) > 2:
                    return False
        return not stack


print(Solution().isValid("({{{{}}}))"))
