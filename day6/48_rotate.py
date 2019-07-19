class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-i-1):
                ni = i
                nj = j
                tmp2 = matrix[ni][nj]
                for k in range(4):
                    nti = nj
                    ntj = n-ni-1
                    tmp1 = matrix[nti][ntj]
                    matrix[nti][ntj] = tmp2
                    tmp2 = tmp1
                    ni = nti
                    nj = ntj
