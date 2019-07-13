class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterdict={'2':'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        if n == 0:
            return []
        out = ['']
        i = 0
        while 1:
            tmp = out.pop(0)
            if len(tmp) > i:
                i += 1
            if i == n:
                out.insert(0,tmp)
                break
            for letter in letterdict[digits[i]]:
                out.append(tmp+letter)
        return out
