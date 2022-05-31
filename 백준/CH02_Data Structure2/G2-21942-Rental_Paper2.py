"""
속도 개선
"""
from sys import stdin
from collections import defaultdict
from datetime import datetime


input = lambda: stdin.readline().rstrip()


def convert(l):
    day, arg = l.split('/')
    day = int(day)
    hour, min = map(int, arg.split(':'))
    total_min = min + hour * 60 + day * 24 * 60
    return total_min


def cal(t1, t2) -> int:
    term = t2 - t1
    d = term.days
    m = term.seconds // 60
    time = d * 24 * 60 + m

    if time > L:
        return (time - L) * F
    return 0


if __name__ == "__main__":
    N, L, F = input().split()
    N, L, F = int(N), convert(L), int(F)
    rental = defaultdict(dict)
    fees = defaultdict(int)

    for _ in range(N):
        query = list(input().split())
        time = datetime.strptime(query[0] + '/' + query[1], '%Y-%m-%d/%H:%M')

        if query[2] in rental[query[3]]:
            fee = cal(rental[query[3]][query[2]], time)
            if fee > 0:
                fees[query[3]] += fee
            del rental[query[3]][query[2]]
        else:
            rental[query[3]][query[2]] = time

    if not fees:
        print(-1)
    else:
        for name in sorted(fees):
            print(name, fees[name], sep=' ')
