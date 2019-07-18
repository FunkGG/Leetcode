class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [''] * 9
        for i in range(9):
            line = ''
            if i % 3 == 0:
                cube = [''] * 3
            for j in range(9):
                cube_j = j // 3
                num = board[i][j]
                if num in line:
                    return False
                elif num != '.':
                    line += num
                if num in row[j]:
                    return False
                elif num != '.':
                    row[j] += num
                if num in cube[cube_j]:
                    return False
                elif num != '.':
                    cube[cube_j] += num
        return True
