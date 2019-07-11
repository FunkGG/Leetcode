class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                ans[j] += ans[j-1]
        return ans[-1]
