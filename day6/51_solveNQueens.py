class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = "." * n

        def put(tmp, colunms, leans1, leans2, i):
            if i == n:
                res.append(tmp)
                return None
            for j in range(n):
                if j not in colunms and j-i not in leans1 and i+j not in leans2:
                    put(tmp+[s[:j] + "Q" + s[j+1:]], colunms+[j], leans1+[j-i], leans2+[i+j], i+1)
                    
        put([],[], [], [], 0)
        return res
