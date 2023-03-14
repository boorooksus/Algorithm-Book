from sys import stdin
input = lambda: stdin.readline().rstrip()


def count_odd(x: str) -> int:
    cnt = 0
    for char in x:
        if int(char) % 2 == 1:
            cnt += 1
    return cnt


def cal(x: str, cnt: int) -> None:
    global min_val, max_val

    cnt += count_odd(x)

    if len(x) == 1:
        min_val, max_val = min(min_val, cnt), max(max_val, cnt)

    if len(x) == 2:
        cal(str(int(x) // 10 + int(x) % 10), cnt)

    else:
        for i in range(1, len(x) - 1):
            for j in range(i + 1, len(x)):
                cal(str(int(x[:i]) + int(x[i:j]) + int(x[j:])), cnt)


if __name__ == "__main__":
    N = input()
    min_val, max_val = int(10e10), 0

    cal(N, 0)
    print(min_val, max_val)
