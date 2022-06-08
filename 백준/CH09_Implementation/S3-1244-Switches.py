from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n = int(input())
    switch = [0] + list(map(int, input().split()))
    m = int(input())
    students = list(list(map(int, input().split())) for _ in range(m))

    for sex, num in students:
        if sex == 1:
            for i in range(num, n + 1, num):
                switch[i] = ~switch[i] + 2
        else:
            switch[num] = ~switch[num] + 2
            left, right = num - 1, num + 1
            while left > 0 and right <= n and switch[left] == switch[right]:
                switch[left] = ~switch[left] + 2
                switch[right] = ~switch[right] + 2
                left -= 1
                right += 1

    for i in range(1, n + 1):
        print(switch[i], end=' ')
        if i % 20 == 0:
            print()

