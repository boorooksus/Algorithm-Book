class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

sol = Solution()
print(sol.hammingWeight(11))

"""
leetcode: 191
비트연산자를 이용한 풀이2
n-1 값과 n을 AND연산 하면 n에서 1이 하나 사라진다.
이렇게 n이 0으로 될때까지 반복하면 반복횟수만큼 1이 있다는 뜻이다.
"""