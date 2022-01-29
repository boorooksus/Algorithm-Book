from sys import stdin


class Solution:
    def palindrome(self, word: str) -> int:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                if word[left + 1:right + 1:] == word[right:left:-1] or \
                        (left > 0 and word[left:right] == word[right - 1:left - 1:-1]) or \
                        (left == 0 and word[:right] == word[right - 1::-1]):
                    return 1

                else:
                    return 2
            left += 1
            right -= 1
        return 0


def input():
    return stdin.readline().strip()


def main():
    t = int(input())
    s = Solution()
    for _ in range(t):
        print(s.palindrome(input()))


if __name__ == "__main__":
    main()
