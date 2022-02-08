"""
참고: https://ddiyeon.tistory.com/81
보드에서 시간별로 4개 상태가 반복됨을 이용
"""

from sys import stdin


r = c = n = 0
board = []
bomb1, bomb2 = [], []
dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, 1, -1]


# 첫 번째 폭탄이 폭발한 후 보드를 'bomb1'에 저장
def explode_bomb1() -> None:
    global bomb1

    bomb1 = [['O'] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == 'O':
                for i in range(5):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < r and 0 <= nx < c:
                        bomb1[ny][nx] = '.'


# 두 번째 폭탄이 폭발한 후 보드를 'bomb2'에 저장
def explode_bomb2() -> None:
    global bomb2

    bomb2 = [['O'] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if bomb1[y][x] == 'O':
                for i in range(5):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < r and 0 <= nx < c:
                        bomb2[ny][nx] = '.'


def main():
    def input():
        return stdin.readline().rstrip()

    global r, c, n, board, dq

    r, c, n = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    # n이 짝수인 경우, 모든 칸에 폭탄이 있음
    if n % 2 == 0:
        for i in range(r):
            print('O' * c)
        return

    # n이 홀수인 경우

    # n이 1일 땐, 초기 상태 출력
    elif n == 1:
        for li in board:
            print(''.join(li))
        return

    # 첫 번째 폭탄 폭발 후 상태 출력
    explode_bomb1()
    if n % 4 == 3:
        for li in bomb1:
            print(''.join(li))
        return

    # 두 번째 폭탄 폭발 후 상태 출력
    explode_bomb2()
    if n % 4 == 1:
        for li in bomb2:
            print(''.join(li))


if __name__ == "__main__":
    main()
