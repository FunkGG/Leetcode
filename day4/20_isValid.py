class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3}
        ans = []
        for i in s:
            if i in d:
                tmp = d[i]
                if 0 < tmp :
                    ans.append(tmp)
                elif tmp == -ans[-1]:
                    ans.pop(-1)
                else:
                    return False
        if len(ans) > 1:
            return False
        else:
            return True  
