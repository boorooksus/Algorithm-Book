from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        res = 0
        while True:
            sub = 0
            for task, val in cnt.most_common(n + 1):
                res += 1
                sub += 1

                cnt.subtract(task)
                cnt += Counter()

            if not cnt:
                break

            res += n + 1 - sub

        return res


# print(Solution().leastInterval( ["A","A","A","B","B","B"],0))
print(Solution().leastInterval( ["A","A","A","B","B","B"],2))