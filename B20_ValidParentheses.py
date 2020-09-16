class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif not stack or abs(ord(i) - ord(stack.pop())) > 2:
                return False

        if stack:
            return False

        return True


sol = Solution()
print(sol.isValid("({{{{}}}))"))
print('{', ord('{'))
print(')', ord(')'))