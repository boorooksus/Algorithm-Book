from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        result = 0

        while True:
            temp = 0
            for task, cnt in counts.most_common(n + 1):
                result += 1
                temp += 1
                counts.subtract(task)
                # 개수가 0 이하인 task 제거
                counts += Counter()

            if not counts:
                break

            # idle 필요한 경우 추가
            result += n + 1 - temp

        return result


print(Solution().leastInterval(["A","A","A","B","B","B"], 2))