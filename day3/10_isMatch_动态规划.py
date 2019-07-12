class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i== len(s)
            first = i<len(s) and p[j] in {s[i], '.'}
            if j < len(p)-1 and p[j+1] == '*':
                result = dp(i, j+2) or (first and dp(i+1, j))
            else:
                result = first and dp(i+1, j+1)
            memo[(i,j)] = result
            return result
        return dp(0,0)
