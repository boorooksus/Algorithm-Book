class Solution:
    def getSum(self, a: int, b: int) -> int:
        def getSum(a, b):
            carry = 0
            result = ""

            for i in range(11):
                x, y = a & 1, b & 1

                if x == 0 and y == 0:
                    result += str(carry)
                    carry = 0
                elif x == 1 and y == 0:
                    result += str(x ^ carry)
                    carry = x & carry
                elif x == 0 and y == 1:
                    result += str(y ^ carry)
                    carry = y & carry
                elif x == 1 and y == 1:
                    result += str(carry)
                    carry = 1

                a = a >> 1
                b = b >> 1
            return result[::-1]

        result = getSum(a, b)
        ans = int(result, 2)
        if result[0] == '1':
            ans ^= 0b11111111111
            result = getSum(ans, 1)
            ans = -int(result, 2)

        return ans


print(Solution().getSum(-12, -8))
