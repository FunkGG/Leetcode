class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        a = ['(']
        lab = [(1,n-1)]
        for i in range(2*n - 1):
            for j in range(len(a)):
                tmp = a.pop(0)
                tmplab, m = lab.pop(0)
                if m:
                    a.append(tmp+'(')
                    lab.append((tmplab+1,m-1))
                if tmplab:
                    a.append(tmp+')')
                    lab.append((tmplab-1, m))
        return a
