class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1 :
                    obstacleGrid[i][j] = 0
                else:
                    if i>0 :
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j>0 :
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
