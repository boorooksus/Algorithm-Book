"""
이전 코드 간결하게 줄임
시간 초과
"""
from sys import stdin
from heapq import heappop, heappush, heapify


def main():
    n, m = map(int, stdin.readline().split())
    # 리스트의 각 원소를 [누적 대기 시간, 심사대 기본 시간] 으로 저장
    t = [[int(stdin.readline())] * 2 for _ in range(n)]

    heapify(t)
    total = 0
    while m > 0:
        total, time = heappop(t)
        heappush(t, [total + time, time])
        m -= 1

    print(total)


if __name__ == "__main__":
    main()
