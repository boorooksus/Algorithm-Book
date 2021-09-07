from typing import List
import heapq


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        hq = []

        for i in range(len(gas)):
            heapq.heappush(hq, [(cost[i] - gas[i]), i])

        while hq:
            tank = 0
            cur = heapq.heappop(hq)[1]
            idx = 0
            while idx < len(gas):
                tank += gas[(cur + idx) % len(gas)]

                if tank < cost[(cur + idx) % len(gas)]:
                    break

                tank -= cost[(cur + idx) % len(gas)]
                idx += 1

            if idx == len(gas):
                return cur

        return -1

# print(Solution().canCompleteCircuit( [1,2,3,4,5], [3,4,5,1,2]))
print(Solution().canCompleteCircuit( [2,3,4], [3,4,3]))

"""
leetcode: 134
"""

