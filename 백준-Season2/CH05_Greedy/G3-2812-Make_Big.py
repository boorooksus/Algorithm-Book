from sys import stdin
input = lambda: stdin.readline().rstrip()


def remove_num(num: str, n: int, k: int) -> str:
    if k == 0:
        return num

    for i in range(n - 1):
        if int(num[i]) < int(num[i + 1]):
            return remove_num(num[:i] + num[i + 1:], n - 1, k - 1)
    return remove_num(num[:-1], n - 1, k - 1)


if __name__ == "__main__":
    N, K = map(int, input().split())
    num_str = input()

    print(remove_num(num_str, N, K))


"""
메모리 초과
자리의 숫자가 바로 뒤의 숫자보다 작으면 제거.
이 방식을 K번 만큼 재귀적으로 진행.
K번 전에 해당되는 숫자가 없어지면 뒤에서 부터 제거
"""