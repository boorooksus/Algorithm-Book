from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_pal(x: str) -> bool:
            start, end = 0, len(x) - 1
            while start < end:
                if x[start] != x[end]:
                    return False
                start += 1
                end -= 1
            return True

        ans = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_pal(words[i] + words[j]):
                    ans.append([i, j])
                if is_pal(words[j] + words[i]):
                    ans.append([j, i])
        return ans


sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))


"""
leetcode: 336
브루트포스 풀이. 시간 초과
"""