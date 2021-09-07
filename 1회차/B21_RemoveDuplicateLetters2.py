from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            seen.add(char)
            stack.append(char)

        return ''.join(stack)

# leetcode: 316
# 스택을 이용한 풀이.(이전 풀이보다 좀 더 빠름)
# Counter, 집합 자료형