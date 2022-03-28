from sys import stdin


def main():
    def input() -> str:
        return stdin.readline().rstrip()

    n = int(input())
    cranes = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    boxes = sorted(list(map(int, input().split())), reverse=True)

    if boxes[0] > cranes[0]:
        print(-1)
        return

    time, cnt = 0, 0
    visit = [False] * m
    loc = [0] * n
    while cnt < m:
        time += 1
        for i in range(len(cranes)):
            while loc[i] < m and (visit[loc[i]] or boxes[loc[i]] > cranes[i]):
                loc[i] += 1

            if loc[i] < m:
                visit[loc[i]] = True
                loc[i] += 1
                cnt += 1

    print(time)


if __name__ == "__main__":
    main()
