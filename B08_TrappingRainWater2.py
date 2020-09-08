from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # height 리스트 원소의 인덱스 저장
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만났을 때
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼냄
                top = stack.pop()
                # 스택이 비어있으면 break
                if not len(stack):
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                water = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * water

            stack.append(i)
        return volume

# leetcode: 42
# 스택 이용
# 이해 잘 안됨. 나중에 다시 볼 것