class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = 0
        if dividend == 0:
            return 0
        sign = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        d = abs(dividend)
        s = abs(divisor)
        m = s
        i = 1
        while d >= s:
            m=s
            i=1
            while d >= m:
                d -= m
                n += i
                m <<= 1
                i <<= 1
        if not sign:
            n = -n
        return min(max(-2 ** 31, n), 2 ** 31 - 1)
