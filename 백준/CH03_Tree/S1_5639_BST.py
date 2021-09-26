from sys import stdin, setrecursionlimit
from typing import List
setrecursionlimit(10 ** 9)


def get_postorder(nums: List) -> List:
    if len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):
        if nums[i] > nums[0]:
            return get_postorder(nums[1:i]) + get_postorder(nums[i:]) + [nums[0]]

    return get_postorder(nums[1:]) + [nums[0]]


nums = []
while True:
    try:
        num = int(stdin.readline())
        nums.append(num)
    except:
        break

for num in get_postorder(nums):
    print(num)
