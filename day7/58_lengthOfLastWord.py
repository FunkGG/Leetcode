class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] != ' ':
                for j in range(i,-2,-1):
                    if j == -1 or s[j] == ' ':
                        return i-j
        return 0
