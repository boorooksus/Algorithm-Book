import sys


def check(ps: str) -> bool:
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        ps = sys.stdin.readline().strip()
        if check(ps):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main()


