from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans: List[List[int]] = []

        def dfs(cur: List[int], left: int):
            if left == 0:
                temp = sorted(cur[:])
                if temp not in ans:
                    ans.append(temp)

            for i in candidates:
                if left - i >= 0:
                    cur.append(i)
                    dfs(cur, left - i)
                    cur.pop()

        dfs([], target)
        return ans

# leetcode: 39
# 조합, dfs, 백트래킹
# 11줄에 원소 이미 존재하는지 체크할 필요 없이
# dfs candidate 범위를 전체가 아닌 현재 숫자부터 돌려도 된다.
