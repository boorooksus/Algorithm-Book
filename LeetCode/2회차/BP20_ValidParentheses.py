class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif i == "]":
                if not stack or stack.pop() != "[":
                    return False

        if stack:
            return False
        return True


sol = Solution()
print(sol.isValid("(]"))

# leetcode: 20
