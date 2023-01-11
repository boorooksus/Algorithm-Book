from sys import stdin
from collections import deque


input = stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input.split())

    dq = deque(i for i in range(1, N + 1))
    ans = []
    while dq:
        dq.rotate(-K + 1)
        ans.append(dq.popleft())

    print('<' + ', '.join(map(str, ans)) + '>')

"""
deque를 이용한 풀이
join()을 활용한 문자열 출력 유용
"""
