from sys import stdin


def prefix_sum(left: int, right: int) -> int:
    return prefix[right] - prefix[left - 1]


n = int(stdin.readline())
honey = [0] + list(map(int, stdin.readline().split()))
prefix = list(0 for _ in range(n + 1))
for i in range(1, len(prefix)):
    prefix[i] = prefix[i - 1] + honey[i]

result = 0
for i in range(2, n):
    # case1: [bee, ... , hive, ... , bee]
    # i: location of hive
    result = max(result,
                 prefix_sum(2, i) + prefix_sum(i, n - 1))
    # case2: [bee, ... , bee, .. , hive]
    # i: location of second bee
    result = max(result,
                 prefix_sum(2, n) + prefix_sum(i + 1, n) - honey[i])
    # case3: [hive, ... , bee, ... , bee]
    # i: location of first bee
    result = max(result,
                 prefix_sum(1, n - 1) + prefix_sum(1, i - 1) - honey[i])

print(result)

"""
서브태스크 배점 100점
시간복잡도: O(N)
"""
