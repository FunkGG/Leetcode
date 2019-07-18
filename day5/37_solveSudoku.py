class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[],[],[],[],[],[],[],[],[]]
        columns = [[],[],[],[],[],[],[],[],[]]
        cubes = [[[],[],[]],
                 [[],[],[]],
                 [[],[],[]]]
        allNum = set(str(i) for i in range(1,10))
        blacks = []
        for i in range(9):
            row = rows[i]
            cube_i = i//3
            for j in range(9):
                column = columns[j]
                cube_j = j//3
                cube = cubes[cube_i][cube_j]
                num = board[i][j]
                if num == '.':
                    blacks.append((i,j))
                    continue
                else:
                    row.append(num)
                    column.append(num)
                    cube.append(num)

        numindex={}
        n = 0
        while n < len(blacks):
            i, j = blacks[n]
            row = rows[i]
            cube_i = i//3
            column = columns[j]
            cube_j = j//3
            cube = cubes[cube_i][cube_j]
            num = board[i][j]
            if num != '.':
                row.remove(num)
                column.remove(num)
                cube.remove(num)
                board[i][j]='.'
            nums = allNum.difference(set(row + column +cube))
            nums = list(nums)
            nums.sort()
            if (i, j) in numindex:
                index = numindex[(i, j)] + 1
            else:
                index = 0
            if index < len(nums):
                num = nums[index]
                board[i][j] = num
                row.append(num)
                column.append(num)
                cube.append(num)
                n += 1
                numindex[(i,j)] = index
            else:
                n -= 1
                numindex[(i, j)] = -1
