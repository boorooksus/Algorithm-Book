from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            for j in range(i, i + len(gas)):
                idx = j % len(gas)
                tank += gas[idx]
                if tank < cost[idx]:
                    break
                tank -= cost[idx]
                if j == i + len(gas) - 1:
                    return i
        return -1


print(Solution().canCompleteCircuit([1,2,3,4,5],
[3,4,5,1,2]))