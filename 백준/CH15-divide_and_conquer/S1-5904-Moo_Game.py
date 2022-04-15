from sys import stdin


def moo(g: int, e: int):
    global N

    if g == 0:
        return ['m', 'o'][N != 1]

    temp = (e - g - 3) // 2  # 이전 군의 길이
    # 3개의 파트로 나눈다.
    # 이전 군 / mooo...ooo / 이전 군
    if N <= temp:
        return moo(g - 1, temp)
    elif temp < N <= temp + g + 3:
        return ['m', 'o'][N - temp != 1]
    else:
        N -= temp + g + 3
        return moo(g - 1, temp)


if __name__ == "__main__":
    N = int(stdin.readline().rstrip())

    # N이 속한 군수열을 구한다.
    # group: N이 속한 군, element: 해당 군의 항 개수
    group, element = 0, 3
    while element < N:
        group += 1
        element = 2 * element + group + 3

    print(moo(group, element))



"""
3
3 + (1 + 3) + 3 = 10
10 + (2 + 5) + 10 = 27 
"""
