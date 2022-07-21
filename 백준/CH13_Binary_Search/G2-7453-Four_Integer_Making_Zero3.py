from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))

    ab = sorted([arr[i][0] + arr[j][1] for i in range(n) for j in range(n)])
    cd = sorted([arr[i][2] + arr[j][3] for i in range(n) for j in range(n)])

    ans = 0
    left, right = 0, len(cd) - 1
    while left < len(ab) and right >= 0:
        if ab[left] + cd[right] == 0:
            ab_idx, cd_idx = left + 1, right - 1
            while ab_idx < len(ab) and ab[left] == ab[ab_idx]:
                ab_idx += 1
            while cd_idx >= 0 and cd[right] == cd[cd_idx]:
                cd_idx -= 1
            ans += (ab_idx - left) * (right - cd_idx)
            left, right = ab_idx, cd_idx

        elif ab[left] + cd[right] < 0:
            left += 1
        else:
            right -= 1

    print(ans)