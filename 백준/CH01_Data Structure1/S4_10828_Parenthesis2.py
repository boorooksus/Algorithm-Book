import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        ps = sys.stdin.readline().strip()

        stack = []
        for p in ps:
            if p == '(':
                stack.append(p)
            else:
                if not stack:
                    print("NO")
                    break
                stack.pop()
        else:
            print('YES') if not stack else print('NO')


if __name__ == "__main__":
    main()


