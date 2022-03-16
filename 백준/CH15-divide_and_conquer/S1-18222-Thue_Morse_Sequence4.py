from sys import stdin


def main():
    print(bin(int(stdin.readline()) - 1).count('1') % 2)


if __name__ == "__main__":
    main()

