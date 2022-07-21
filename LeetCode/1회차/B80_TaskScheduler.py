from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        res = 0

        while True:
            temp = 0
            for task, _ in cnt.most_common(n + 1):
                res += 1
                temp += 1
                cnt.subtract(task)
                cnt += Counter()  # 이렇게 하면 0 이하의 항목 제거됨

            if not cnt:
                break

            res += n + 1 - temp

        return res

sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))



"""
leetcode: 621
"""