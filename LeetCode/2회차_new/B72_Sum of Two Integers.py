class Solution:
    def getSum(self, a: int, b: int) -> int:
        save, cur = 0b0, 0b1
        res = ""

        if a < b:
            a, b = b, a

        while b:
            if a & cur == 1 and b & cur == 1:
                res += str(save)
                save = 1
            elif (a | b) & cur == 1:
                if save == 1:
                    save = 1
                    res += '0'
                else:
                    res += '1'
            else:
                res += str(save)
                save = 0

            a >>= 1
            b >>= 1

        while a:
            if save == 1 and a & cur == 1:
                res += '0'
            elif save == 1 and a & cur == 0:
                res += '1'
                save = 0
            else:
                res += str(bin(a & cur))[2:]

            a >>= 1
        res += str(save)

        return int(res[::-1], 2)


print(Solution().getSum(2, 3))

