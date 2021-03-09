from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            for j in range(i, i + len(gas)):
                cur = j % len(gas)

                tank += gas[cur]
                if tank < cost[cur]:
                    i = j + 1
                    break

                if (cur + 1) % len(gas) == i:
                    return i
                tank -= cost[cur]

        return -1


print(Solution().canCompleteCircuit(
[1,2,3,4],
[1,3,4,3]))