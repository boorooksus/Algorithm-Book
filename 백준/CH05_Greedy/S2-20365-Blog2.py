from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    colors = input()

    cnts = {'B': 0, 'R': 0}
    for i in range(N - 1):
        if colors[i] != colors[i + 1]:
            cnts[colors[i]] += 1
    cnts[colors[-1]] += 1

    print(min(cnts.values()) + 1)
