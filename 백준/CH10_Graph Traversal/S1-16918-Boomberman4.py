"""
참고: https://ddiyeon.tistory.com/81
보드에서 시간별로 4개 상태가 반복됨을 이용
이전 코드 간략화
"""

from sys import stdin


r = c = n = 0
# board: 보드의 초기상태, 첫 번째 폭탄 폭발 후 상태, 두 번째 폭탄 폭발 후 상태 저장
board = [[], [], []]
# 폭발 범위 (가운데와 상하좌우)
dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, 1, -1]


def explode_bombs() -> None:
    global board

    # k: 업데이트할 board의 인덱스
    for k in range(1, 3):
        board[k] = [['O'] * c for _ in range(r)]
        for y in range(r):
            for x in range(c):
                # 이전 보드 위치에 폭탄이 있는 경우
                if board[k - 1][y][x] == 'O':
                    # 가운데, 상하좌우 폭발 후를 현재 보드 위치에 저장
                    for i in range(5):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < r and 0 <= nx < c:
                            board[k][ny][nx] = '.'

        # 두 번째 폭발 후 상태를 알 필요 없는 경우
        if n % 4 == 3:
            # 첫 번째 폭발 후 상태만 저장하고 break
            break


def main():
    def input():
        return stdin.readline().rstrip()
    global r, c, n, board

    r, c, n = map(int, input().split())
    board[0] = [list(input()) for _ in range(r)]

    # n이 짝수인 경우, 모든 칸에 폭탄이 있음
    if n % 2 == 0:
        for i in range(r):
            print('O' * c)
        return

    # n이 홀수인 경우
    elif n == 1:
        for li in board[0]:
            print(''.join(li))
        return

    explode_bombs()

    if n % 4 == 3:
        for li in board[1]:
            print(''.join(li))
    else:
        for li in board[2]:
            print(''.join(li))


if __name__ == "__main__":
    main()
