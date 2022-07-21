from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 윈도우: nums의 인덱스 저장(값 아님 주의)
        window, result = deque(), []

        for i in range(len(nums)):
            # 윈도우 오른쪽으로 이동
            if window and i - window[0] == k:
                window.popleft()

            # 윈도우에서 불필요한 숫자 제거
            # 윈도우에서 추가할 숫자보다 작은 값들은 필요 없음
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            # 윈도우에 인덱스 추가
            window.append(i)

            # 최대값 추가
            if i + 1 >= k:
                result.append(nums[window[0]])

        return result


"""
시간 초과 해결 방법
출처: https://github.com/onlybooks/algorithm-interview/issues/67
"""
