from sys import stdin


def get_population(row1, col1, row2, col2) -> int:
    result = 0
    for i in range(row1, row2 + 1):
        result += population[i][col2] - population[i][col1 - 1]
    return result


n, m = map(int, stdin.readline().split())
population = [[0 for _ in range(m + 1)]]
for i in range(n):
    population.append([0] + list(map(int, stdin.readline().split())))
    for j in range(1, m + 1):
        population[-1][j] += population[-1][j - 1]

k = int(stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    print(get_population(x1, y1, x2, y2))
