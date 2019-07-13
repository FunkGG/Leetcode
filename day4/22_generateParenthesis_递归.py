class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n > 0:
            a = []
            for i in range(n):
                for j in self.generateParenthesis(i):
                     a += ['('+j+')'+ans for ans in self.generateParenthesis(n-1-i)]
            return a
        else:
            return ['']
