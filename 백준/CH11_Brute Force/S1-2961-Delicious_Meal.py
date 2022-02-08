from sys import stdin


n: int
ings = []
res = 2e9


def dfs(s: int, b: int, cur) -> None:
    global res

    if cur == n:
        if s != 1 or b != 0:
            res = min(int(abs(s - b)), res)
        return

    dfs(s, b, cur + 1)
    dfs(s * ings[cur][0], b + ings[cur][1], cur + 1)


def main():
    def input():
        return stdin.readline().rstrip()
    global n, ings

    n = int(input())
    for _ in range(n):
        s, b = map(int, input().split())
        ings.append((s, b))

    dfs(1, 0, 0)
    print(res)


if __name__ == "__main__":
    main()
