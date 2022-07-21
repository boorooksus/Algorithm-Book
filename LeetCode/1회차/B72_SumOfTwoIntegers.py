class Solution:
    def getSum(self, a: int, b: int) -> int:
        mark = 0
        if a < 0:
            a = ~a
            mark = 1
        if b < 0:
            b = ~b
            mark = 1

        x, y = bin(a), bin(b)
        idx = -1
        save = 0
        res = []

        while x[idx] != 'b' and y[idx] != 'b':
            temp = save + int(x[idx]) + int(y[idx])
            save = 0
            if temp >= 2:
                save = 1
                temp -= 2
            res.append(temp)
            idx -= 1

        if x[idx] == 'b':
            x = y

        while x[idx] != 'b':
            temp = save + int(x[idx])
            save = 0
            if temp >= 2:
                save = 1
                temp -= 2
            res.append(temp)
            idx -= 1

        if save == 1:
            res.append(1)


        ans = 0
        for i in range(len(res)):
            ans += res[i] * (2 ** i)

        if mark:
            ans -= res[-1] * (2 ** (len(res) - 1))
            ans *= -1
        return ans

        #return int('0b' + ''.join(map(str, reversed(res))))

sol = Solution()
print(sol.getSum(-12, -8))

"""
leetcode: 371
오답.
"""