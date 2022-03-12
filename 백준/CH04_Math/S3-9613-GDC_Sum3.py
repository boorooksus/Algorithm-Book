from sys import stdin


def get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return get_gcd(b, a % b)


def main():
    t = int(stdin.readline())
    for _ in range(t):
        nums = list(map(int, stdin.readline().split()))

        res = 0
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res += get_gcd(nums[i], nums[j])
                else:
                    res += get_gcd(nums[j], nums[i])

        print(res)


if __name__ == "__main__":
    main()
