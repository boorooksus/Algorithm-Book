from sys import stdin


if __name__ == "__main__":
    code = stdin.readline().rstrip()

    if code[0] == '0':
        print(0)
        exit()

    dp = [0] * (len(code) + 2)
    dp[-1], dp[-2] = 1, 1

    for idx in range(len(code) - 1, -1, -1):
        unit = int(code[idx])
        if unit > 0:
            dp[idx] = (dp[idx] + dp[idx + 1]) % 1000000
        if code[idx] != '0' and idx + 1 < len(code):
            unit = int(code[idx] + code[idx + 1])
            if 0 < unit <= 26:
                dp[idx] = (dp[idx] + dp[idx + 2]) % 1000000

    print(dp[0])


"""
중간에 있는 두 자리 숫자를 처리할 때, 0으로 시작하는 경우 예외처리 해야함
ex) 111[01]1111 
"""