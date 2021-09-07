from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for idx, num in enumerate(nums):
            if target - num in num_idx:
                return [idx, num_idx[target - num]]
            num_idx[num] = idx  # == 1 =========================


# leetcode: 01
# 3번 풀이에서 하나의 for문으로 정리. 속도 차이는 거의 없음 but 코드가 깔끔
# 1: 9번째 줄 코드를 7번으로 옮기고 if문에 idx != num_idx[target - num] 조건 추가해도 틀림
#       [3, 3]이 입력으로 주어진 경우 []을 출력함(dict 값이 덮어 씌워지기 때문)
