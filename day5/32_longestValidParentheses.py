class Solution:
    def longestValidParentheses(self, s: str) -> int:
        out = 0
        d = {'(': 1, ')': -1}
        lab = 0
        tmp = 0
        for i in range(len(s)):
            lab += d[s[i]]
            if lab < 0:
                tmp = 0
                lab = 0
            elif lab == 0:
                tmp += 1
                out = max(out, tmp)
            else:
                tmp += 1
        d = {'(': -1, ')': 1}
        lab = 0
        tmp = 0
        for i in range(-1, -len(s)-1, -1):
            lab += d[s[i]]
            if lab < 0:
                tmp = 0
                lab = 0
            elif lab == 0:
                tmp += 1
                out = max(out, tmp)
            else:
                tmp += 1
        return out
