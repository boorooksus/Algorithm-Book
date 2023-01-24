from sys import stdin
input = lambda: stdin.readline().rstrip()


# i: 군, j: 항
def sol(i: int, j: int) -> str:
    if i == 0:
        return ['4', '7'][j == 1]

    if j < 2 ** i:
        return '4' + sol(i - 1, j)
    else:
        return '7' + sol(i - 1, j % 2 ** i)


if __name__ == "__main__":
    K = int(input())

    # i군 j항 구하기
    n, i = 0, 0  # n: 누적 개수
    while n < K:
        i += 1
        n += 2 ** i
    n -= 2 ** i
    i -= 1
    j = K - n - 1

    print(sol(i, j))


"""
1. K의 i군 j항 구한다. (항과 군은 0부터 시작)
    0군: 4(0군 0항) 7(0군 1항)
    1군: 44 47 74 77
    2군: 444 447 474 477 744 747 774 777
    
2. 각 자리별 숫자를 앞자리 부터 재귀적으로 구한다. 
   각 군에 속한 숫자들의 각 자리별 4와 7의 개수는 모두 같다는 점을 이용한다.
   ex) 2군 각 자리의 '4'의 개수: 4개, '7'의 개수 4개
    2-1. 항이 해당 군의 중간보다 작으면 앞자리가 '4', 크면 '7'이 된다
        4xx 4xx ... 4xx | 7xx 7xx ... 7xx
"""
