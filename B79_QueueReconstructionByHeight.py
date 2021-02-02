from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key=lambda x: (x[1], x[0]))
        people.sort(key=lambda x: x[0])

        cur = 0
        while cur < len(people):
            greater = 0
            for i in range(cur):
                if people[i][0] >= people[cur][0]:
                    greater += 1

            if people[cur][1] > greater:
                temp = cur
                while greater < people[cur][1]:
                    if people[temp + 1][0] >= people[cur][0]:
                        greater += 1
                    temp += 1
                people[cur], people[temp] = people[temp], people[cur]

            elif people[cur][1] < greater:
                greater = 0
                for i in range(len(people)):
                    if greater == people[cur][1]:
                        people[cur], people[i] = people[i], people[cur]
                        cur = i + 1
                        break
                    if people[i][0] >= people[cur][0]:
                        greater += 1

            else:
                cur += 1

        return people

sol = Solution()
print(sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))

"""
leetcode: 406
시간초과
"""