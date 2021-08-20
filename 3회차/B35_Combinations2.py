from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(index, path):
            if len(path) == k:
                result.append(path)
                return

            for i in range(index, n + 1):
                dfs(i + 1, path + [i])

        dfs(1, [])
        return result


print(Solution().combine(4, 2))