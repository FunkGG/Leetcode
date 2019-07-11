class Solution:
    def reverseWords(self, s: str) -> str:
        out = ''
        s = ' '+s
        n = len(s)
        i = n-1
        while i>= 0:
            if s[i] ==' ':
                i -= 1
            else:
                j = i-1
                while s[j] != ' ':
                    j -= 1
                    # if j == -1:
                        # break
                out += ' ' + s[j+1:i+1]
                i = j-1
        return out[1:]
