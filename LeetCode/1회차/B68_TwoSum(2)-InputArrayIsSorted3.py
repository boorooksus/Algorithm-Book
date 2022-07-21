from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target % 2 == 0 and numbers.count(target // 2) > 1:
            a = numbers.index(target // 2)
            b = numbers[a + 1:].index(target // 2)
            return [a + 1, b + a + 2]

        numbers_set = sorted(list(set(numbers)))
        for i in range(len(numbers_set) - 1):
            if target - numbers_set[i] in numbers_set[i + 1:]:
                a = numbers.index(numbers_set[i])
                b = a + 1 + numbers[a + 1:].index(target - numbers_set[i])
                return [a + 1, b + 1]

        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
이전 풀이에서 불필요하게 중복된 경우를 제외함
"""