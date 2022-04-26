from sys import stdin


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    colors = input()

    groups = []
    for i, color in enumerate(colors):
        if i < N - 1 and color != colors[i + 1]:
            groups.append(color)
    groups.append(colors[-1])

    blue = groups.count('B')
    print(min(blue, len(groups) - blue) + 1)
