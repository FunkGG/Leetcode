class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]
        nums = [str(i) for i in range(1, n + 1)]
        for i in range(2, n):
            fac.append(i * fac[-1])

        def f1(n, k, s):
            if n > 1:
                divid = fac[n - 2]
                num = k // divid
                tmp = nums.pop(num)
                s += tmp
                return f1(n - 1, k % divid, s)
            else:
                return s + nums[0]
        return f1(n,k-1,'')
