class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows ==1:
            return s
        n = len(s)
        rows = min(n,numRows)
        z = ['']*rows
        row = 0
        for i,sr in enumerate(s):
            z[row] += sr
            if row == rows-1:
                rowNext = -1
            if row == 0:
                rowNext = 1
            row += rowNext
        return ''.join(z)
