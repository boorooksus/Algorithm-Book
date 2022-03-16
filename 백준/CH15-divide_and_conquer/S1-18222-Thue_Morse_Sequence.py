from sys import stdin


def thue_morse(k: int) -> int:
    x = 0
    while True:
        if k < 2 ** (x + 1):
            break
        x += 1

    cnt = 0
    while x > 0:
        if k >= 2 ** x:
            cnt += 1
        k %= 2 ** x
        x -= 1

    if k == 1:
        cnt += 1

    return [0, 1][cnt % 2 == 1]


def main():
    k = int(stdin.readline())
    print(thue_morse(k - 1))


if __name__ == "__main__":
    main()


"""
0 01 0110 01101001 
1 2  4    8       
n번 수행 -> 2 ^ (n - 1)

k번째 값 -> 2 ^ (x - 1) < k <= 2 ^ x

2 ^ x -> !k % (2 ^ (x - 1))
"""