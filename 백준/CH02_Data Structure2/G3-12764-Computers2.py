"""
시간 초과
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    time = list(list(map(int, input().split())) for _ in range(N))

    time.sort()
    cnt = 0
    counter, occupied = {}, {}
    for start, end in time:
        for i in range(1, cnt):
            if occupied[i] <= start:
                counter[i] += 1
                occupied[i] = end
                break
        else:
            cnt += 1
            counter[cnt] = 1
            occupied[cnt] = end

    print(cnt)
    for i in range(1, cnt + 1):
        print(counter[i], end=' ')
