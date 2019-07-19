class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 0
        if n < 0:
            sign = -1
        n = abs(n)
        i = 0
        tmp = x
        j = 1
        out = 1
        while i < n:
            if i+j <= n:
                out *= tmp
                i += j
                tmp *= tmp
                j += j
            else:
                tmp = x
                j = 1
        if sign:
            out = 1/out
        return out
