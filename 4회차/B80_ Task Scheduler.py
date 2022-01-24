from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        res = 0
        while cnt.items():
            i = 0
            order = cnt.most_common()
            while i < n + 1 and cnt.items():
                res += 1
                if i < len(order):
                    cnt[order[i][0]] -= 1
                    if cnt[order[i][0]] == 0:
                        cnt.pop(order[i][0])

                i += 1
        return res


print(Solution().leastInterval(["A","A","A","B","B","B"],
2))
