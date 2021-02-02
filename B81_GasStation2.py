from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fuel, start = 0, 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]:
                start = i + 1
                fuel = 0

            else:
                fuel += gas[i] - cost[i]

        return start

print(Solution().canCompleteCircuit( [1,2,3,4,5], [3,4,5,1,2]))
# print(Solution().canCompleteCircuit( [2,3,4], [3,4,3]))

"""
leetcode: 134
"""

