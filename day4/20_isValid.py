class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3}
        ans = []
        lab = float('inf')

        for i in s:
            if i in d:
                tmp = d[i]
                if 0 < tmp:
                    ans.append(tmp)
                    lab = tmp
                elif tmp == -lab:
                    ans.pop(-1)
                    lab = ans[-1] if ans else float('inf')
                else:
                    return False
        if ans:
            return False
        else:
            return True
