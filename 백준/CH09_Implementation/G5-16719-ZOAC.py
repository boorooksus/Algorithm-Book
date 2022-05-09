from sys import stdin


if __name__ == "__main__":
    x = stdin.readline().rstrip()

    arr = []
    for i, char in enumerate(x):
        arr.append((char, i))

    res = [''] * len(x)
    while arr:
        idx = 0
        res[arr[0][1]] = arr[0][0]
        word = ''.join(res)
        res[arr[0][1]] = ''
        for i in range(1, len(arr)):
            res[arr[i][1]] = arr[i][0]
            temp = ''.join(res)
            if word > temp:
                idx = i
                word = temp
            res[arr[i][1]] = ''
        print(word)
        res[arr[idx][1]] = arr[idx][0]
        del arr[idx]

