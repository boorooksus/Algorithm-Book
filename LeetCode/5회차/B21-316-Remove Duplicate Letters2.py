from collections import Counter, defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), defaultdict(bool), []

        for char in s:
            if seen[char]:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 1:
                seen[stack.pop()] = False
            stack.append(char)
            seen[char] = True

        return ''.join(stack)
