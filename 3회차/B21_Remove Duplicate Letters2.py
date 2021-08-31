from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = Counter(s)
        stack, seen = [], set()

        for char in s:
            counts[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and counts[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)
