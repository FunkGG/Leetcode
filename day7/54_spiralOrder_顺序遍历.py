class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        out = []
        i = 0
        j = 0
        di = 0
        dj = 1
        while len(out) < m*n:
            out.append(matrix[i][j])
            matrix[i][j] = None
            if i+di == m or j+dj == n or matrix[i+di][j+dj] == None:
                tmp = di
                di = dj
                dj = -tmp
            i += di
            j += dj
        return out
