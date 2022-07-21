from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt, stack, done = Counter(s), [], []

        for char in s:
            cnt[char] -= 1

            if char in done:
                continue

            while stack and stack[-1] > char and cnt[stack[-1]] > 0:
                done.remove(stack.pop())

            stack.append(char)
            done.append(char)

        return ''.join(stack)
