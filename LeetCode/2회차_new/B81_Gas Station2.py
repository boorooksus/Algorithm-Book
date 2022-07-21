from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0, 0
        for i in range(len(gas)):
            fuel += gas[i]
            if fuel < cost[i]:
                fuel = 0
                start = i + 1
            else:
                fuel -= cost[i]

        return start


print(Solution().canCompleteCircuit(
[1,2,3,4],
[1,3,4,3]))