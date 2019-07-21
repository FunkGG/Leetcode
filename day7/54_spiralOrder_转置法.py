class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        out = matrix.pop(0)
        
        while matrix:
            matrix = [list(i) for i in zip(*matrix)]
            matrix.reverse()
            out += matrix.pop(0) 
        return out
