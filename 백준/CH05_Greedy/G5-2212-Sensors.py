from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n, k = (int(input()) for _ in range(2))
    sensors = sorted(list(map(int, input().split())))

    if k >= n:
        print(0)
        return

    dists = sorted(list(sensors[i + 1] - sensors[i] for i in range(n - 1)), reverse=True)
    print(sum(dists[k - 1:]))


if __name__ == "__main__":
    main()

