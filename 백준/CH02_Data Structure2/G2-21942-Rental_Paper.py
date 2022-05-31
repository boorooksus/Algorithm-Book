from sys import stdin
from re import sub
from collections import defaultdict
from datetime import datetime


input = lambda: stdin.readline().rstrip()


def cal(d1: str, hm1: str, d2: str, hm2: str) -> int:
    t1 = datetime.strptime(d1 + '/' + hm1, '%Y-%m-%d/%H:%M')
    t2 = datetime.strptime(d2 + '/' + hm2, '%Y-%m-%d/%H:%M')

    diff = (t2 - t1).total_seconds() // 60
    if diff > L:
        return (diff - L) * F
    return 0


if __name__ == "__main__":
    N, L, F = input().split()
    temp = list(map(int, sub(r'[/|:]', ' ', L).split()))
    N, L, F = int(N), temp[2] + temp[1] * 60 + temp[0] * 60 * 24, int(F)
    people = defaultdict(list)
    fees = defaultdict(int)
    for _ in range(N):
        query = list(input().split())

        for i, [tool, d, hm] in enumerate(people[query[3]]):
            if tool == query[2]:
                fee = cal(d, hm, query[0], query[1])
                if fee > 0:
                    fees[query[3]] += fee
                del people[query[3]][i]
                break
        else:
            people[query[3]].append((query[2], query[0], query[1]))

    if not fees:
        print(-1)
    else:
        for name in sorted(fees):
            print(name, fees[name], sep=' ')
