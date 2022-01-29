from sys import stdin


word: str = ''


def palindrome(left: int, right: int, del_cnt: int) -> int:
    global word

    if del_cnt == 2:
        return del_cnt

    while left < right:
        if word[left] != word[right]:
            a = palindrome(left + 1, right, del_cnt + 1)
            b = palindrome(left, right - 1, del_cnt + 1)
            return a if a < b else b
        left += 1
        right -= 1
    return del_cnt


def input():
    return stdin.readline().strip()


def main():
    global word

    t = int(input())
    for _ in range(t):
        word = input()
        print(palindrome(0, len(word) - 1, 0))


if __name__ == "__main__":
    main()
