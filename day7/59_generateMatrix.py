class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(1, n * n + 1):
            ans[x][y] = i
            if ans[(x + dx) % n][(y + dy) % n] > 0:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return ans
