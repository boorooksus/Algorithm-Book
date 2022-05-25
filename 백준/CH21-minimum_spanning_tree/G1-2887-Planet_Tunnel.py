from sys import stdin


input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    # if x == y:
    #     return
    parents[x] += parents[y]
    parents[y] = x


def kruscal() -> int:
    tunnels = []
    # 모든 간선이 아닌 각 좌표별로 거리를 구한다.
    # 각 좌표를 기준으로 오름차순 정렬을 했을때,
    # X1->X2가 X1->X3보다 클 수 없다.
    for i in range(3):
        planets.sort(key=lambda x: x[i])
        for j in range(1, N):
            tunnels.append((abs(planets[j - 1][i] - planets[j][i]),
                            planets[j - 1][3], planets[j][3]))

    res = 0
    tunnels.sort()
    for cost, a, b in tunnels:
        a, b = find(a), find(b)
        if a != b:
            res += cost
            union(a, b)
            # if parents[a] == -N:
            #     break
    return res


if __name__ == "__main__":
    N = int(input())
    planets = [list(map(int, input().split())) + [i] for i in range(N)]
    parents = [-1] * N
    print(kruscal())
