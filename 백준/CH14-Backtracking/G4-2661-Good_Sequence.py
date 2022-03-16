from sys import stdin


nums = ['1', '2', '3']


def check(x: str) -> bool:
    for left in range(len(x)):
        for size in range(1, (len(x) - left) // 2 + 1):
            right = left + size
            if x[left:right] == x[right:right + size]:
                return False
    return True


def dfs(cur: str, n: int) -> str:
    if not check(cur):
        return ''

    if len(cur) == n:
        return cur

    for num in nums:
        res = dfs(cur + num, n)
        if res:
            return res


def main():
    n = int(stdin.readline())

    print(dfs('', n))


if __name__ == "__main__":
    main()
