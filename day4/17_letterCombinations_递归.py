class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterdict={'2':'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        out = []
        if n == 0:
            return out
        def f(i, ans):
            if i < n:
                for letter in letterdict[digits[i]]:
                    f(i+1, ans+letter)
            else:
                out.append(ans)
        f(0, '')
        return out
